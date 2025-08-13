# Repository Guidelines

## Project Structure & Module Organization
- `ds/`: Core data structures (linked list, queues).
- `sorting/`, `searching/`, `trees/`: Algorithm implementations and small runners.
- `cses/`, `usaco/`, `hrt/`: Problem-specific solutions and experiments.
- `htmlStuff/`: Small HTML/JS visuals for concepts.
- Mixed languages: Python 3, C++11 (`.cpp`), and a minimal Java stub (`Main.java`).

## Build, Test, and Development Commands
- `make all`: Compile and run every `*.cpp` it finds into `build/` and execute each.
- `make clean`: Remove `build/` artifacts.
- `make cses/melon`: Compile and run a specific C++ file (path without extension).
- `python3 sorting/quicksort.py`: Run Python scripts directly; most files include inline demos.
- `javac Main.java && java Main`: Build and run the Java stub if needed.

## Coding Style & Naming Conventions
- Python: 4-space indents, PEP 8 naming (`snake_case` for functions, `CamelCase` for classes). Keep files lower-case, descriptive (e.g., `trees/binary_tree.py`).
- C++: Target C++11, keep functions and files lower_snake_case; place quick demos in `main()` in the same file.
- Scripts: One-off problem files may use short, descriptive names (e.g., `cses/max_dist.py`). Prefer clarity over brevity.
- Comments: Prefer brief, intent-focused comments and small, testable functions.

## Testing Guidelines
- Current tests are lightweight/in-file. Add quick assertions or sample I/O under `if __name__ == "__main__":` (Python) or a small `main()` (C++).
- Optional: colocate simple tests as `*_test.py` next to modules. If adopting `pytest`, run with `python3 -m pytest`.
- Aim for examples that cover edge cases (empty inputs, single element, sorted/reverse-sorted arrays).

## Commit & Pull Request Guidelines
- Commits: Short, imperative summaries (e.g., "add heapsort partition fix", "clean up"). Group related changes.
- PRs: Keep focused; include problem link (if applicable), approach summary, complexity, and run instructions. Add sample input/output or screenshots for HTML demos.

## Security & Configuration Tips
- No external secrets or credentials should be committed. Keep datasets and large outputs out of the repo. Use `make clean` before sharing.
