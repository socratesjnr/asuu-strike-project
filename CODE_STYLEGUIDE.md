# Code Style Guide

This programming style guide is intended to provide guidelines for writing clear, maintainable, and consistent code for the data science project investigating the impact of the 2022 ASUU strike on academic performance at the University of Lagos. This guide covers the Python programming language.

## Table of Contents

- [Code Style Guide](#code-style-guide)
  - [Table of Contents](#table-of-contents)
  - [Naming Conventions](#naming-conventions)
  - [Formatting Guidelines](#formatting-guidelines)
  - [Documentation Standards](#documentation-standards)
  - [Best Practices](#best-practices)
  - [Regular Review and Revision](#regular-review-and-revision)

## Naming Conventions

1. Use meaningful and descriptive variable names that reflect their purpose.

   ```python
   ## ✔ Do this
   expanded_sample = pd.concat([sample_df]*200, ignore_index=True)

   ## ❌ Not this
   exp_sample = pd.concat([sample_df]*200, ignore_index=True)
   ```

2. Variables, functions, and file names should use lowercase letters separated by underscores.

   ```python
   ## ✔ Do this
   expanded_sample.to_csv("expanded_sample.csv", index=False)

   ## ❌ Not this
   exp_sample.to_csv("Expanded_Sample.csv", index=False)
   exp_sample.to_csv("Expanded Sample.csv", index=False)
   exp_sample.to_csv("ExpandedSample.csv", index=False)
   ```

    Note: Markdown files (`.md`) are an exception to this rule. Use UPPERCASE letters separated by underscores instead.

    ```markdown
    **✔ Do this**
        CODE_STYLEGUIDE.md
        README.md
        CONTRIBUTORS.md</p>

    **❌ Not this** 
        Code Style Guide.md
        code_style_guide.md
        readme.md
        contributrs.md
    ```

3. Use singular nouns for variables that represent a single item and plural nouns for variables that represent collections of items.

    ```python
    # ✔ Do this
    scores = list(df["student_score"])

    # ❌ Not this
    score = list(df["student_score"])
   ```

4. Include a variable type if there are multiple variables with the same name but different datatypes.

    ```python
    # ✔ Do this
    matric_str = input("What is your matric number?")
    matric_int = int(matric_str)

    # ❌ Not this
    matric = input("What is your matric number?")
    matric_no = int(matric)
   ```

5. Class names should use PascalCase.

      ```python
    # ✔ Do this
    class MyClass: 
            pass

    # ❌ Not this
    class my_class: 
            pass
   ```

6. Commonly used variable names are allowed but their use should be limited. For example:
   - `var`, `id`, `i`, `n`, etc may be used as identifiers or counters in loops
   - `df` may be used if the file predominantly uses a single dataframe
  
7. Use lowercase letters separated by hyphens for directory names.

      ```python
    # ✔ Do this
    'mock-analysis/test_model.ipynb'

    # ❌ Not this
    'Mock Analysis/test_model.ipynb'
   ```  

## Formatting Guidelines

1. Use four spaces for indentation.
2. Avoid lines longer than 79 characters.
3. Use blank lines to separate code blocks logically.
4. Use whitespace judiciously to make code more readable.

## Documentation Standards

1. Use comments to explain code logic and reasoning.
2. Use docstrings to document functions and classes.
3. Use clear and descriptive variable names that make it easy to understand their purpose.

## Best Practices

1. Follow PEP 8 guidelines for Python coding.
2. Use version control to track changes and collaborate with team members.
3. Write unit tests to verify the correctness of functions and methods.
4. Use meaningful variable names that make the code self-documenting.
5. Avoid magic numbers and define them as constants instead.

## Regular Review and Revision

This style guide should be reviewed and updated as needed throughout the project. Team members are encouraged to provide feedback and suggest revisions to ensure that the style guide remains relevant and effect.
