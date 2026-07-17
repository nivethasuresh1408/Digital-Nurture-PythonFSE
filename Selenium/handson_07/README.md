## Page Object Model (POM)

In a flat Selenium script, every test contains locators and UI interaction code.
If the Submit button ID changes from `submit` to `btn-submit`, every test that uses that locator must be updated individually.

Using the Page Object Model, the locator exists only once inside the Page class.
Only that single locator needs to be updated, while all test cases continue to work without modification.

This improves:
- Reusability
- Readability
- Maintainability
- Scalability