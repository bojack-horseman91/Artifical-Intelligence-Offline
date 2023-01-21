def doDepthFirstSearch(current, neighbor_time_slot):
    """
    This function is used to find all the nodes in the kempe-chain
    """
    # Mark the current node as visited
    current.set_dfs_status(1)
    
    # Get all the neighboring nodes that overlap with current node
    overlapping_courses = current.get_overlapping_courses()
    
    # Iterate through all the neighboring nodes
    for i in range(len(overlapping_courses)):
        # If the neighboring node is not visited and has the same time slot as the neighbor_time_slot
        if overlapping_courses[i].get_dfs_status() == 0 and overlapping_courses[i].get_time_slot() == neighbor_time_slot:
            # Perform DFS on that neighboring node
            doDepthFirstSearch(overlapping_courses[i], current.get_time_slot())
    
    # Mark the current node as completely visited
    current.set_dfs_status(2)
    return
