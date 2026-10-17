"use strict";

// NEXORA: Search tools
function searchTools() {
const searchInput = document.getElementById("toolSearch");
const toolCards = document.querySelectorAll(".tool-card");
const noResults = document.getElementById("noResults");

```
if (!searchInput || !noResults) return;

const searchText = searchInput.value.toLowerCase().trim();
let foundTools = 0;

toolCards.forEach(function (card) {
    const toolName = (card.dataset.name || "").toLowerCase();
    const cardText = card.textContent.toLowerCase();
    const matches =
        searchText === "" ||
        toolName.includes(searchText) ||
        cardText.includes(searchText);

    card.hidden = !matches;

    if (matches) {
        foundTools++;
    }
});

noResults.hidden = foundTools !== 0;
```

}

// Run search when the user types or clicks Search
document.addEventListener("DOMContentLoaded", function () {
const searchInput = document.getElementById("toolSearch");
const searchButton = document.getElementById("searchButton");

```
if (searchInput) {
    searchInput.addEventListener("input", searchTools);

    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            searchTools();
        }
    });
}

if (searchButton) {
    searchButton.addEventListener("click", searchTools);
}
```

});

// Profit Calculator
function calculateProfit() {
const revenueInput = document.getElementById("revenue");
const expensesInput = document.getElementById("expenses");
const result = document.getElementById("result");

```
if (!revenueInput || !expensesInput || !result) return;

if (
    revenueInput.value.trim() === "" ||
    expensesInput.value.trim() === ""
) {
    result.textContent = "Please enter both revenue and expenses.";
    return;
}

const revenue = Number(revenueInput.value);
const expenses = Number(expensesInput.value);

if (
    !Number.isFinite(revenue) ||
    !Number.isFinite(expenses) ||
    revenue < 0 ||
    expenses < 0
) {
    result.textContent = "Please enter valid non-negative numbers.";
    return;
}

const profit = revenue - expenses;

if (profit > 0) {
    result.textContent = "Net Profit: " + profit.toFixed(2);
} else if (profit < 0) {
    result.textContent = "Net Loss: " + Math.abs(profit).toFixed(2);
} else {
    result.textContent = "Break-even: no profit or loss.";
}
```

}
