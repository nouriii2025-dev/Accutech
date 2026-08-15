document.addEventListener("DOMContentLoaded", () => {
  // Mobile nav toggle
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      links.classList.toggle("open");
      const expanded = links.classList.contains("open");
      toggle.setAttribute("aria-expanded", expanded ? "true" : "false");
    });
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => links.classList.remove("open"))
    );
  }

  // Highlight active nav link
  const path = window.location.pathname.replace(/\/$/, "") || "/";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const href = a.getAttribute("href").replace(/\/$/, "") || "/";
    if (href === path) a.classList.add("active");
  });

  // Scroll-reveal animations
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("in"));
  }
});


// ============================================================
// DATABASE-DRIVEN PRODUCT SECTION
// ============================================================

let PRODUCT_CATEGORIES = [];
let PRODUCTS = [];

const state = {
    category: "",
    subcategory: "",
    productType: "",
    brands: new Set()
};


// ------------------------------------------------------------
// Load product data from Django
// ------------------------------------------------------------

async function loadProductData() {
    try {
        console.time("PRODUCT DATA");
        const response = await fetch("/products/data/");
        console.timeEnd("PRODUCT DATA");

        if (!response.ok) {
            throw new Error(
                `Failed to load products: ${response.status}`
            );
        }

        const data = await response.json();

        PRODUCT_CATEGORIES = data.categories || [];
        PRODUCTS = data.products || [];

        buildMegaMenu();
        populateCategorySelect();
        populateSubcategorySelect();
        populateProductTypeSelect();
        populateBrandList();
        render();

    } catch (error) {
        console.error("Product data loading error:", error);

        const grid = document.getElementById("psGrid");
        const empty = document.getElementById("psEmpty");

        if (grid) {
            grid.innerHTML = `
                <div class="ps-empty">
                    Unable to load products. Please try again later.
                </div>
            `;
        }

        if (empty) {
            empty.style.display = "none";
        }
    }
}


// ------------------------------------------------------------
// Mega menu
// ------------------------------------------------------------

function buildMegaMenu() {
    const grid = document.getElementById("psMegaGrid");

    if (!grid) return;

    grid.innerHTML = "";

    const cols = [[], [], []];

    PRODUCT_CATEGORIES.forEach((category, index) => {

        const col = document.createElement("div");
        col.className = "ps-mega-col";

        const categoryLink = document.createElement("a");

        categoryLink.className = "ps-cat";

        categoryLink.href =
            "#products?category=" +
            encodeURIComponent(category.name);

        categoryLink.textContent = category.name;

        col.appendChild(categoryLink);


        category.subcategories.forEach(subcategory => {

            const subLink = document.createElement("a");

            subLink.className = "ps-sub";

            subLink.href =
                "#products?category=" +
                encodeURIComponent(category.name) +
                "&sub=" +
                encodeURIComponent(subcategory.name);

            subLink.textContent = subcategory.name;

            col.appendChild(subLink);


            subcategory.product_types.forEach(productType => {

                const typeLink = document.createElement("a");

                typeLink.className = "ps-leaf";

                typeLink.href =
                    "#products?category=" +
                    encodeURIComponent(category.name) +
                    "&sub=" +
                    encodeURIComponent(subcategory.name) +
                    "&type=" +
                    encodeURIComponent(productType.name);

                typeLink.textContent = productType.name;

                col.appendChild(typeLink);
            });
        });

        cols[index % 3].push(col);
    });


    cols.forEach(colGroup => {

        const wrapper = document.createElement("div");

        wrapper.className = "ps-mega-col-wrapper";

        colGroup.forEach(col => {
            wrapper.appendChild(col);
        });

        grid.appendChild(wrapper);
    });


    const navItem = document.getElementById("psNavItem");
    const trigger = document.getElementById("psNavTrigger");

    if (trigger && navItem) {

        trigger.addEventListener("click", () => {

            navItem.classList.toggle("open");

            trigger.setAttribute(
                "aria-expanded",
                navItem.classList.contains("open")
                    ? "true"
                    : "false"
            );
        });

        document.addEventListener("click", event => {

            if (!navItem.contains(event.target)) {
                navItem.classList.remove("open");
            }

        });
    }
}


// ------------------------------------------------------------
// Category filter
// ------------------------------------------------------------

function populateCategorySelect() {

    const select = document.getElementById("psCategory");

    if (!select) return;

    select.innerHTML =
        `<option value="">All Categories</option>`;

    PRODUCT_CATEGORIES.forEach(category => {

        const option = document.createElement("option");

        option.value = category.name;
        option.textContent = category.name;

        select.appendChild(option);
    });


    select.onchange = () => {

        state.category = select.value;

        state.subcategory = "";
        state.productType = "";

        populateSubcategorySelect();
        populateProductTypeSelect();

        render();
    };
}


// ------------------------------------------------------------
// Subcategory filter
// ------------------------------------------------------------

function populateSubcategorySelect() {

    const select = document.getElementById(
        "psSubcategory"
    );

    if (!select) return;

    select.innerHTML =
        `<option value="">All Sub Categories</option>`;


    const category = PRODUCT_CATEGORIES.find(
        item => item.name === state.category
    );

    if (!category) return;


    category.subcategories.forEach(subcategory => {

        const option = document.createElement("option");

        option.value = subcategory.name;
        option.textContent = subcategory.name;

        select.appendChild(option);
    });


    select.onchange = () => {

        state.subcategory = select.value;

        state.productType = "";

        populateProductTypeSelect();

        render();
    };
}


// ------------------------------------------------------------
// Product type filter
// ------------------------------------------------------------

function populateProductTypeSelect() {

    const select = document.getElementById(
        "psProductType"
    );

    if (!select) return;

    select.innerHTML =
        `<option value="">All Product Types</option>`;


    const category = PRODUCT_CATEGORIES.find(
        item => item.name === state.category
    );

    if (!category) return;


    const subcategory = category.subcategories.find(
        item => item.name === state.subcategory
    );

    if (!subcategory) return;


    subcategory.product_types.forEach(productType => {

        const option = document.createElement("option");

        option.value = productType.name;
        option.textContent = productType.name;

        select.appendChild(option);
    });


    select.onchange = () => {

        state.productType = select.value;

        render();
    };
}


// ------------------------------------------------------------
// Brand filter
// ------------------------------------------------------------

function populateBrandList() {

    const list = document.getElementById("psBrandList");

    if (!list) return;

    list.innerHTML = "";


    const brands = [
        ...new Set(
            PRODUCTS
                .map(product => product.brand)
                .filter(Boolean)
        )
    ].sort();


    brands.forEach(brand => {

        const label = document.createElement("label");

        const checkbox = document.createElement("input");

        checkbox.type = "checkbox";
        checkbox.value = brand;


        checkbox.addEventListener("change", () => {

            if (checkbox.checked) {
                state.brands.add(brand);
            } else {
                state.brands.delete(brand);
            }

            render();
        });


        label.appendChild(checkbox);

        label.appendChild(
            document.createTextNode(brand)
        );

        list.appendChild(label);
    });
}


// ------------------------------------------------------------
// Filter matching
// ------------------------------------------------------------

function matchesFilters(product) {

    if (
        state.category &&
        product.category !== state.category
    ) {
        return false;
    }


    if (
        state.subcategory &&
        product.subcategory !== state.subcategory
    ) {
        return false;
    }


    if (
        state.productType &&
        product.product_type !== state.productType
    ) {
        return false;
    }


    if (
        state.brands.size &&
        !state.brands.has(product.brand)
    ) {
        return false;
    }


    return true;
}


// ------------------------------------------------------------
// Product icon
// ------------------------------------------------------------

function productIcon() {

    return `
        <svg
            viewBox="0 0 24 24"
            fill="none"
        >
            <rect
                x="4"
                y="4"
                width="16"
                height="16"
                rx="2"
                stroke="currentColor"
                stroke-width="1.5"
            />

            <path
                d="M8 9h8M8 13h5"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linecap="round"
            />
        </svg>
    `;
}


// ------------------------------------------------------------
// Render products
// ------------------------------------------------------------

function render() {

    const grid = document.getElementById("psGrid");
    const empty = document.getElementById("psEmpty");
    const count = document.getElementById("psResultCount");

    if (!grid) return;


    const filteredProducts =
        PRODUCTS.filter(matchesFilters);


    if (count) {
        count.textContent = filteredProducts.length;
    }


    grid.innerHTML = "";


    if (empty) {
        empty.style.display =
            filteredProducts.length
                ? "none"
                : "block";
    }


    filteredProducts.forEach(product => {

        const card = document.createElement("div");

        card.className = "ps-card";


        const imageHTML = product.image
            ? `
                <img
                    src="${product.image}"
                    alt="${product.name}"
                >
              `
            : productIcon();


        card.innerHTML = `
            <div class="ps-card-img">
                ${imageHTML}
            </div>

            <div class="ps-card-body">

                <div class="ps-card-brand">
                    ${product.brand || ""}
                </div>

                <div class="ps-card-title">
                    ${product.name}
                </div>

                <div class="ps-card-cat">
                   Model: ${product.model_number || ""}
                </div>

                <div class="ps-card-cta">
                    View details →
                </div>

            </div>
        `;


        card.addEventListener(
            "click",
            () => openModal(product)
        );


        grid.appendChild(card);
    });
}


// ------------------------------------------------------------
// Product detail modal
// ------------------------------------------------------------

function openModal(product) {

    document.getElementById(
        "psModalBrand"
    ).textContent = product.brand || "";


    document.getElementById(
        "psModalTitle"
    ).textContent = product.name;


    document.getElementById(
        "psModalPath"
    ).textContent = [
        product.category,
        product.subcategory,
        product.product_type
    ]
        .filter(Boolean)
        .join(" / ");


    document.getElementById(
        "psModalDesc"
    ).textContent =
        product.description ||
        product.short_description ||
        "";


    const image =
        document.getElementById("psModalImage");

    const placeholder =
        document.getElementById(
            "psModalImagePlaceholder"
        );


    if (product.image) {

        image.src = product.image;
        image.alt = product.name;
        image.style.display = "block";

        if (placeholder) {
            placeholder.style.display = "none";
        }

    } else {

        image.src = "";
        image.style.display = "none";

        if (placeholder) {
            placeholder.style.display = "block";
        }
    }


    const specs =
        document.getElementById(
            "psModalSpecs"
        );


    specs.innerHTML = "";


    Object.entries(
        product.specifications || {}
    ).forEach(([key, value]) => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${key}</td>
            <td>${value}</td>
        `;

        specs.appendChild(row);
    });


    const datasheetLink =
        document.querySelector(
            '.ps-modal-actions a[href="#datasheet"]'
        );


    if (datasheetLink) {

        if (product.datasheet) {

            datasheetLink.href =
                product.datasheet;

            datasheetLink.style.display =
                "inline-flex";

        } else {

            datasheetLink.removeAttribute(
                "href"
            );

            datasheetLink.style.display =
                "none";
        }
    }


    document
        .getElementById("psModalOverlay")
        .classList.add("open");
}


// ------------------------------------------------------------
// Close modal
// ------------------------------------------------------------

function closeModal() {

    const modal =
        document.getElementById(
            "psModalOverlay"
        );

    if (modal) {
        modal.classList.remove("open");
    }
}


const modalClose =
    document.getElementById(
        "psModalClose"
    );

if (modalClose) {
    modalClose.addEventListener(
        "click",
        closeModal
    );
}


const modalOverlay =
    document.getElementById(
        "psModalOverlay"
    );

if (modalOverlay) {

    modalOverlay.addEventListener(
        "click",
        event => {

            if (
                event.target === modalOverlay
            ) {
                closeModal();
            }

        }
    );
}


document.addEventListener(
    "keydown",
    event => {

        if (event.key === "Escape") {
            closeModal();
        }

    }
);


// ------------------------------------------------------------
// Clear filters
// ------------------------------------------------------------

const clearButton =
    document.getElementById(
        "psClear"
    );

if (clearButton) {

    clearButton.addEventListener(
        "click",
        () => {

            state.category = "";
            state.subcategory = "";
            state.productType = "";

            state.brands.clear();


            const category =
                document.getElementById(
                    "psCategory"
                );

            const subcategory =
                document.getElementById(
                    "psSubcategory"
                );

            const productType =
                document.getElementById(
                    "psProductType"
                );


            if (category) {
                category.value = "";
            }

            if (subcategory) {
                subcategory.value = "";
            }

            if (productType) {
                productType.value = "";
            }


            document
                .querySelectorAll(
                    "#psBrandList input"
                )
                .forEach(
                    checkbox =>
                        checkbox.checked = false
                );


            populateSubcategorySelect();
            populateProductTypeSelect();

            render();
        }
    );
}


// ------------------------------------------------------------
// INIT
// ------------------------------------------------------------

if (
    document.getElementById("psGrid")
) {
    loadProductData();
}
