def get_unfulfilled_requests(total_resources: int, n: int, requests: list[list[int]]) -> list[int]:
    # Step 1: Initialize a set with all request IDs
    unfulfilled = {req[0] for req in requests}

    # Step 2: Sort the requests
    # key=lambda x: (-x[2], x[3], x[0]) means:
    # 1. -x[2]: requestBid DESCENDING (by making it negative)
    # 2. x[3]: requestTimestamp ASCENDING
    # 3. x[0]: requestID ASCENDING (tie-breaker)
    requests.sort(key=lambda x: (-x[2], x[3], x[0]))

    i = 0

    # Step 3: Process identical bids group by group
    while i < n and total_resources > 0:
        j = i
        # Find the boundary of the current bid group
        while j < n and requests[j][2] == requests[i][2]:
            j += 1

        # The original group is already sorted by Timestamp ASC
        group_orig = requests[i:j]

        # Sort a copy of the group by Quantity ASC for the bulk math allocation
        group_by_qty = sorted(group_orig, key=lambda x: x[1])

        already_given = 0
        active_k = len(group_orig)

        for req in group_by_qty:
            if total_resources == 0:
                break

            req_id, req_qty = req[0], req[1]

            # Difference needed to fulfill this specific request
            diff = req_qty - already_given

            # If it was already fulfilled in a previous bulk operation
            if diff <= 0:
                unfulfilled.discard(req_id)
                active_k -= 1
                continue

            # Resources needed to give `diff` to all currently active members
            needed = active_k * diff

            if total_resources >= needed:
                total_resources -= needed
                already_given += diff
                unfulfilled.discard(req_id)
                active_k -= 1
            else:
                # We don't have enough to fulfill the current target.
                # Distribute whatever is left evenly using integer division (//).
                base = total_resources // active_k
                rem = total_resources % active_k

                already_given += base
                total_resources = 0

                # Distribute remainder strictly based on earliest timestamp
                for orig_req in group_orig:
                    if rem == 0:
                        break

                    orig_id, orig_qty = orig_req[0], orig_req[1]

                    # If this request is still active (unfulfilled)
                    if orig_id in unfulfilled:
                        # Does this 1 remainder unit perfectly fulfill them?
                        if already_given + 1 == orig_qty:
                            unfulfilled.discard(orig_id)
                        rem -= 1

                break # Resources are depleted

        i = j # Move to the next bid group

    # Return the list of remaining unfulfilled request IDs
    return list(unfulfilled)