# 236. Lowest Common Ancestor of a Binary Tree (Medium)
#
# Video explanation: https://www.youtube.com/watch?v=6B6xk-ZqWN8
#
# Given a binary tree (NOT a BST, so values are in no order) and two nodes p and q,
# return their lowest common ancestor (LCA): the LOWEST node that has both p and q
# below it. A node counts as a descendant of itself, so p can be the LCA of p and q.
#
# (For a BST you can use the ordering instead, see
#  ../11-binary-search-trees/lowest-common-ancestor-of-a-bst.py
#  and "binary tree vs BST" in ../11-binary-search-trees/README.md.)
#
# =====================================================================================
# KEY IDEA (in my words)
# =====================================================================================
#
#   Go all the way to the BOTTOM first, then pass answers back UP (post-order).
#   Each node returns ONE thing to its parent:
#
#     - None              -> "I found NEITHER p nor q down here"
#     - p (or q)          -> "I found p (or q) down here"
#     - the LCA itself    -> "I already found BOTH, here is the answer"
#
#   We keep returning None to the upper node TILL we see either p or q.
#
#     - If only p is found  -> return p up (it is the ancestor so far)
#     - If only q is found  -> return q up (it is the ancestor so far)
#     - If BOTH come back (one from left, one from right)
#                           -> THIS node is where they meet: return this node.
#                              Every node above just passes it up untouched.
#     - If NEITHER is found -> None goes up, all the way to the root,
#                              and the root also returns None.
#
#   The 4 cases at a node, after asking both children:
#
#     left    right   | return
#     --------------- | --------------------------------------------
#     None    None    | None   (nothing found below me)
#     X       None    | X      (pass up what the left side found)
#     None    X       | X      (pass up what the right side found)
#     X       Y       | me     (p on one side, q on the other -> I am the LCA)
#
# =====================================================================================

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------------------------------------------------------------------
# My solution (the 4 cases written out)
# -------------------------------------------------------------------------------------
def lowestCommonAncestor(root, p, q):
    def dfs(root, p, q):
        if not root:                      # stepped PAST a leaf (the None level)
            return None                   # nothing found here
        if root == p or root == q:        # found one of them
            return root                   # send it up (no need to look below, see "Why we can stop at p" below)

        left = dfs(root.left, p, q)       # go to the bottom of the left side first
        right = dfs(root.right, p, q)     # then the bottom of the right side

        # ---- now coming back UP: decide what to tell my parent ----
        if left and right:                # p came from one side, q from the other
            return root                   # -> I am the lowest common ancestor
        if right and not left:            # only the right side found something
            return right                  # pass it up
        if left and not right:            # only the left side found something
            return left                   # pass it up
        # neither side found anything -> implicitly returns None
    return dfs(root, p, q)


# -------------------------------------------------------------------------------------
# Same thing, shorter (how he finishes the code in the video: `return left || right`)
# -------------------------------------------------------------------------------------
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            # base cases
            if node is None:
                return None
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right          # whichever one is not None (or None if both are None)
                                          # covers the other 3 cases in one line
        return dfs(root)


# =====================================================================================
# THE VIDEO'S ILLUSTRATION  (Example 1: p = 5, q = 1, answer = 3)
# =====================================================================================
#
# He draws the tree, then puts N at every empty spot BELOW the leaves (the None level,
# one step past the last level), and draws an arrow from each child back UP to its
# parent with what that child returns.
#
#   [x] = what that node returns UP to its parent (his red arrows),  N = None
#
#                            3  [3]  <- got 5 from the left AND 1 from the right
#                         /     \        -> BOTH -> 3 is the LCA (he circles it)
#                       /         \
#              [5]  5                1  [1]
#                 /   \            /   \
#          [N]  6       2  [N]   0 [N]  8 [N]
#              / \     / \      / \    / \
#             N   N   7   4    N   N  N   N
#                   [N]   [N]
#                   / \   / \
#                  N   N N   N
#
#   Read it BOTTOM -> UP:
#
#   1. The N's at the very bottom: `if not root: return None`.
#   2. 6: left N, right N, 6 is not p or q            -> returns N to 5
#   3. 7: N, N                                        -> returns N to 2
#      4: N, N                                        -> returns N to 2
#      2: gets N and N                                -> returns N to 5
#   4. 5: everything below returned N, BUT 5 == p     -> returns 5 to 3
#         (he wrote next to it: "is (p or q)? return root")
#   5. 0: N, N                                        -> returns N to 1
#      8: N, N                                        -> returns N to 1
#      1: 1 == q                                      -> returns 1 to 3
#   6. 3: left gave 5, right gave 1, BOTH not None    -> 3 is the LCA (he circles it)
#
#   NOTE: in his drawing he walks below 5 (6, 2, 7, 4) to show how N travels up.
#   The CODE never goes below 5: `if root == p or root == q: return root` runs BEFORE
#   the recursive calls, so as soon as it reaches 5 it returns 5 without looking at
#   6, 2, 7, 4. Same for 1 (it never visits 0 and 8). The answer is the same either way.
#
#   Time:  O(N)  each node is visited at most once
#   Space: O(N)  the call stack (height of the tree; N in the worst case, a straight line)
#
# =====================================================================================
# DRY RUN OF THE CODE (what actually runs)  p = 5, q = 1
# =====================================================================================
#
#   call          what happens                                  returns
#   ------------  --------------------------------------------  -------
#   dfs(3)        3 is not p/q -> go left
#     dfs(5)      5 == p -> stop here                           5
#   dfs(3)        left = 5 -> now go right
#     dfs(1)      1 == q -> stop here                           1
#   dfs(3)        right = 1. left AND right -> return node      3   <- answer
#
# =====================================================================================
# DRY RUN 2  (Example 2: p = 5, q = 4, answer = 5)  q is UNDER p
# =====================================================================================
#
#                     3
#                   /   \
#                 [5]    1          p = 5
#                 / \   / \
#                6   2 0   8
#                   / \
#                  7  [4]           q = 4  (inside 5's subtree)
#
#   call          what happens                                  returns
#   ------------  --------------------------------------------  -------
#   dfs(3)        not p/q -> go left
#     dfs(5)      5 == p -> stop, never looks at 4               5
#   dfs(3)        left = 5 -> go right
#     dfs(1)      not p/q -> left
#       dfs(0)    N, N                                          None
#       dfs(8)    N, N                                          None
#     dfs(1)      None, None                                    None
#   dfs(3)        left = 5, right = None -> pass up left        5   <- answer
#
# Why we can stop at p (and not look for q below it):
#   The problem promises p and q are BOTH in the tree.
#   - If q were somewhere else (not under p), the OTHER side of some ancestor would
#     find it and that ancestor would return itself (the "both" case).
#   - Nobody else found q (the right side of 3 returned None), so q MUST be under p.
#     Then p is the lowest node that has both -> p is the answer. A node is its own
#     descendant.
#
# =====================================================================================
# DRY RUN 3  (neither found: say p and q are not in this tree)
# =====================================================================================
#
#        1
#       / \          every leaf returns None, every parent gets None/None
#      2   3         and returns None, so the root returns None as the final answer.
#
#   (LeetCode never gives this case, but it shows what "None goes all the way up" means.)
#
# =====================================================================================
# Common mistakes
# =====================================================================================
#   - Comparing values instead of nodes is fine on LeetCode (values are unique), but
#     p and q are TreeNodes, so `root == p` is the natural check.
#   - Writing `return root` at the end instead of `return left or right`: that would
#     return a node even when nothing was found below it.
#   - Forgetting `if not root: return None` first. See the rules of tree recursion in
#     README.md.


if __name__ == "__main__":
    # Example tree: [3,5,1,6,2,0,8,null,null,7,4]
    n7, n4 = TreeNode(7), TreeNode(4)
    n6, n2 = TreeNode(6), TreeNode(2, n7, n4)
    n0, n8 = TreeNode(0), TreeNode(8)
    n5, n1 = TreeNode(5, n6, n2), TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    for f in (lowestCommonAncestor, Solution().lowestCommonAncestor):
        assert f(root, n5, n1) is root      # Example 1 -> 3
        assert f(root, n5, n4) is n5        # Example 2 -> 5
        assert f(root, n7, n4) is n2        # both under 2 -> 2
        assert f(root, n6, n4) is n5        # 6 left of 5, 4 under 2 -> 5
        assert f(root, n0, n7) is root      # different sides of 3 -> 3
    print("all good")
