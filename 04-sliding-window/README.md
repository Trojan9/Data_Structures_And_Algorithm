# Sliding Window

Grow the right edge, shrink the left edge while the window is invalid. Turns O(n^2) substring problems into O(n).

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [longest-substring-without-repeating-characters](longest-substring-without-repeating-characters.py) | Set of chars in window; shrink from left on duplicate | | ✅ |
| [longest-substring-without-repeating-characters-bloomberg](longest-substring-without-repeating-characters-bloomberg.py) | Same problem, Bloomberg-folder version | ✅ | |
| [longest-repeating-character-replacement](longest-repeating-character-replacement.py) | Valid while window length - max count <= k | | ✅ |
| [minimum-window-substring](minimum-window-substring.py) | Grow until have == need, then shrink from the left | | ✅ |
