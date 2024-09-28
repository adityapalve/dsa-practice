# Compiler
CXX := g++

# Compiler flags
CXXFLAGS := -std=c++11 -Wall -Wextra

# Build directory
BUILD_DIR := build

# # Default target
# all: $(BUILD_DIR)

# # Ensure build directory exists
# $(BUILD_DIR):
# 	mkdir -p $(BUILD_DIR)

# # Rule to compile and run .cpp file
# %.run: %.cpp | $(BUILD_DIR)
# 	$(CXX) $(CXXFLAGS) $< -o $(BUILD_DIR)/$*
# 	@$(BUILD_DIR)/$*

# # Clean rule
# clean:
# 	rm -rf $(BUILD_DIR)

# # Phony targets
# .PHONY: all clean


# Find all .cpp files in the current directory and subdirectories
CPP_FILES := $(shell find . -name "*.cpp")

# Create corresponding .run targets
# RUN_TARGETS := $(patsubst %.cpp,%.run,$(CPP_FILES))
TARGETS := $(patsubst %.cpp,%,$(CPP_FILES))

# Rule to compile and run .cpp file
%: %.cpp
	@mkdir -p $(dir $(BUILD_DIR)/$@)
	$(CXX) $(CXXFLAGS) $< -o $(BUILD_DIR)/$@
	@$(BUILD_DIR)/$@

# Clean rule
clean:
	rm -rf $(BUILD_DIR)

# Phony targets
.PHONY: clean all

all: $(TARGETS)

# Make all targets phony to ensure they always run
.PHONY: force 
force:

$(TARGETS): force