# PROMPT: REMOVE ALL SAMPLE DATA FROM KRISHIMITRA AI

Act as a senior full-stack developer and modify my existing KrishiMitra AI website.

## 1. Remove All Sample Data

* Remove all sample values, demo data, placeholder numbers, hardcoded crop details, and predefined market prices.
* Do not automatically fill any form with sample values.
* All input fields must be empty by default, except for dropdowns that contain actual category options.
* Remove messages such as "Sample values for demonstration. Replace them with your own."
* Never display fake crop yields, farming costs, market prices, profits, or predictions.

## 2. Fix the Crop Calculator

* Allow users to enter their own land area, unit, crop name, expected yield, selling price, and cultivation cost.
* Make every required numeric field empty by default.
* Validate inputs before calculating.
* Calculate total yield, total revenue, total cultivation cost, and estimated profit using only the user's entered values.
* Formula:
   * Total yield = Land area × Yield per acre.
   * Total revenue = Total yield × Price per quintal.
   * Total cost = Land area × Cost per acre.
   * Estimated profit = Total revenue − Total cost.
* Display a clear message if any required field is missing or invalid.
* Do not generate results until the user clicks Calculate.

## 3. Fix Market Price Comparison

* Remove all hardcoded market prices and fake market information.
* Allow users to enter actual market names and prices manually, or retrieve current market prices from a working, reliable API.
* If live market data is unavailable, clearly state "Market price data unavailable. Please enter verified market prices manually."
* Never invent prices or display demonstration values as real market data.

## 4. Fix the Frontend JavaScript

* Preserve the existing KrishiMitra AI UI, layout, colors, buttons, and responsive design.
* Use HTML, CSS, and vanilla JavaScript without requiring a backend.
* Ensure the Calculate and Compare Markets buttons work correctly.
* Fix JSON parsing errors, including errors caused by attempting to parse HTML as JSON.
* Check HTTP response status and content type before parsing API responses.
* Handle missing data, invalid inputs, network errors, and unavailable APIs gracefully.
* Do not show fake successful results when an operation fails.

## 5. Remove Misleading Predictions

* Do not use hardcoded yield changes, price changes, or artificial low/high estimates.
* If the user has not supplied sufficient information for a calculation, request the missing information.
* Clearly label estimates calculated from user inputs as estimates, not guaranteed outcomes.

## 6. Final Requirements

* Modify the existing project instead of creating a completely new website.
* Do not redesign the existing UI.
* Do not introduce sample data anywhere in the application.
* Do not break existing working features.
* Test every calculator and market comparison button.
* Ensure all results are generated from user inputs or verified live data only.

**Expected result:** A fully functional KrishiMitra AI website with empty input fields, no sample data, accurate calculations based on user inputs, reliable market comparisons, and clear error messages.
