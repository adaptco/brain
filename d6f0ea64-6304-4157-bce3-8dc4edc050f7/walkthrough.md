# Unit Testing Walkthrough

## Completed Changes

### Makefile Update

I updated the `Makefile` to include a `test_engine` target. This allows compiling and running the `tests/engine_test.cpp` file while linking against the engine object files (excluding `main.o` to prevent conflicts).

[Makefile](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/Makefile)

```makefile
test_engine: $(OBJS)
 # Filter out main.o if it exists in OBJS to avoid multiple main() definitions
 $(CXX) $(CXXFLAGS) tests/engine_test.cpp $(filter-out $(BUILD_DIR)/src/main.o, $(OBJS)) -o $(BIN_DIR)/engine_test
 ./$(BIN_DIR)/engine_test
```

### Engine Test Verification

I verified that `tests/engine_test.cpp` correctly uses the `WorldModel` API:

- `LoadLevel(int)`
- `GetCurrentLevel()`

These methods are present in `src/engine/WorldModel.hpp`.

## Verification Status
>
> [!WARNING]
> **Skipped**: Verification could not be run locally because `g++` and `make` are not installed or accessible on the system.

Expected usage once tools are available:

```bash
make test_engine
```
