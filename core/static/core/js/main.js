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


// Product section
const PRODUCT_TAXONOMY = {
  "Pressure Measurement": {
    "Pressure Gauges": ["Commercial Pressure Gauges","Industrial Pressure Gauges","Process Pressure Gauges","Low Pressure Gauges","Diaphragm Gauges","High Precision Test Gauges","Differential and Duplex Pressure Gauges","Absolute Pressure Gauges"],
    "Pressure Gauges with Transmitter Switches": ["Pressure Gauges with Electrical Output Signal","Pressure Gauges with Switch Contacts"],
    "Pressure Switches": ["Mechanical Pressure Switches"],
    "Pressure Transmitters": ["Pressure Transducer and Transmitter","Submersible Pressure Transmitter","Electronic Pressure Switches","Explosion Proof Pressure Transmitters","Intelligent Bus Compatible","Process Transmitters","Digital Gauge"],
    "Diaphragm Seals": ["Threaded Process Connections","Flanged Connection","Sterile Connection","Hydra-Line Diaphragm Seal Systems","Diaphragm Seal Accessories"]
  },
  "Temperature Measurement": {
    "Thermowells": ["Thermowells"],
    "Mechanical Temperature Measurement": ["Bimetallic Thermometers","Expansion Thermometers","Gas Actuated Thermometers","Machine Glass Thermometers"],
    "Temperature Gauges with Transmitter Switches": ["Dial Thermometers with Electrical Output Signal","Dial Thermometers with Switch Contacts"],
    "Temperature Switches": ["Mechanical Temperature Switches"],
    "Electrical Temperature Measurement": ["Temperature Transmitters","Resistance Thermometers","Thermocouples","Electrical Temperature Switches"]
  },
  "Controllers Indicators and Recorders": {
    "Indicator": ["Panel Mounted Digital Indicators","Field Mounted Digital Indicators","Attachable Indicators"],
    "Controllers": ["Panel Mounted Controllers"],
    "Recorders": ["Videographic Recorders","Circular Chart Recorders","Strip Chart Recorders"]
  },
  "Level Measurement": {
    "Mechanical Level Measurement": ["Magnetic Level Gauges","Mini Tubular Level Gauges","Oil Level Gauge","Float and Board Tank Gauge","Float and Dial Gauge","Weld Pad Flat Glass Level Gauge","Transparent Tubular Level Gauge","Reflex Transparent Flat Glass Level Gauge"],
    "Level Switches": ["Buoyancy Level Switches","RF Capacitance Level Switches","Vibrating Fork Level Switches","Conductivity Type Level Switch with Control Unit","Thermal Dispersion Type","Air Operated","Rotary Paddle Level Switch","Vibrating Diamond Blade Level Switch","Vibrating Rod Level Switch"],
    "Level Transmitters": ["Magnetic Float Operated Guided","RF Capacitance Type Level Transmitter","Electronic Level Switch with Display","Magnetostrictive Level Transmitters","Guided Wave Radar Level Transmitters","Ultrasonic Level Transmitters and Switches","Laser Level Transmitters","Gauge and Differential Pressure Level Transmitters","Displacer Level Transmitter","Radar Level Transmitter"]
  },
  "Flow Measurement": {
    "Mechanical Flow Measurement": ["Variable Area Flow Meters"],
    "Flow Transmitters": ["Coriolis Mass Flow Meters","Inline Mass Flow Meters","Insertion Mass Flow Meters","Electromagnetic Flow Meters","Flow Computer Units","Thermal Mass Flow Meters","Vortex and Swirl Flow Meters","Ultrasonic Flow Meters","Primary Flow Differential Products","Turbine Type Flow Meters"]
  },
  "Calibration Technology": {
    "Pressure": ["Portable Pressure Generation","Hand-Held Calibrators","Precision Pressure Measuring Instruments","Pressure Controllers","Pressure Balances"],
    "Temperature": ["Reference Thermometers","Hand Held Calibrators","Digital Hand-Held Multimeter","Process Calibrator RTD","Process Calibrator Temperature","Process Calibrator Thermocouple","Portable Temperature Calibrators","Calibration Baths"],
    "Current Voltage Resistance": ["High Precision Process Calibrator","Hand Held Multifunction Calibrator","Documenting Multi Function Calibrator","Hand Held Temperature Calibrator","Portable multi-function calibrator","Precision Loop Calibrator","Process Calibrator Current Voltage"],
    "Humidity": ["High Precision Humidity Calibrator","Humidity Calibration Set"]
  },
  "Valves and Fittings": {
    "Needle Valve": ["Single Bonnet","Double Bonnet","High Pressure","Angle","Medium Pressure"],
    "Gauge Valves": ["Gauge Bleed Valve","Gauge Vent Valve","Multiport Gauge Valve","Forged Body Gauge Valve"],
    "Ball Valves": ["1000 WOG","3000 WOG","10000 PSI Standard Bore Ball Valves"],
    "Manifold Valves": ["Two Valve Manifolds","Three Valve Manifolds","Five Valve Manifolds","Double Block and Bleed Manifolds"],
    "Check Valves": ["22,500 PSI Check Valves","High Pressure Check Valves","10,000 PSI Check Valves"],
    "Instrumentation Pipe Fitting": ["Straights","Elbows Tees and Crosses"],
    "Instrumentation Tube Fitting": ["Straights","Elbows Tees and Crosses"],
    "High Pressure Tube Fittings": ["Straights","Elbows Tees and Crosses"],
    "Pressure Gauge Accessories": ["Pressure Gauge Cocks","Over Pressure Protectors","Swivel Adaptors","Syphons","Pressure Gauge Snubbers"],
    "Instrumentation Tubes": ["Standard","High Pressure"],
    "Relief Valves": []
  },
  "Food and Pharma": {
    "Pumps": ["Positive Displacement Pumps","Centrifugal Pumps","Side Channel Pumps"],
    "Filters and Sight Glass": ["Filters","Sight Glass","Filter Regulator"],
    "Mixing Equipment": ["Agitators","Mixers","Blenders"],
    "Fittings": ["Unions","Elbows","Tees","Reducers","Tubes"],
    "Valves": ["Butterfly Valves","Seat Valves","Diaphragm Valves","Process Valves"],
    "Skids": ["Mixing and Blending","CIP Systems","Heat Treatment","Product Recovery","Valve Manifolds","More Skids"]
  },
  "Pressure Regulator": {
    "": ["High Pressure Regulator","Two Stage Regulator","Relief & Back Pressure","UHP Core Valve","Low Pressure Regulator","Precision Regulator","Inline and Y Type Filters"]
  }
};

// Brands as listed on the reference site's filter panel
const BRANDS = ["Wika","Winters","Accutech","Trafag","ABB","Wika/Cella","E+E","Techtrol","Kirchner & Tochter","Racine","Mueller","Inoxpa","Alco-Valves","Maximator","Alco","Insert Deal","Drastar","Land Ametek","AccuClean"];

/* =========================================================================
   SAMPLE PRODUCT DATA — placeholder only.
   The live site loads real product records via AJAX per sub-category,
   which isn't exposed in static HTML. Replace PRODUCTS with your real
   dataset (Django queryset -> JSON, or a fetch() to your API).
   Shape is intentionally simple so it's a drop-in swap.
========================================================================= */
const PRODUCTS = [
  { id:1, name:"Bourdon Tube Pressure Gauge 232.50", brand:"Wika", category:"Pressure Measurement", subcategory:"Pressure Gauges", leaf:"Industrial Pressure Gauges",
    desc:"Copper alloy Bourdon tube gauge for general industrial applications, standard connection sizes and dial diameters.",
    specs:{ "Dial size":"63 / 100 / 160 mm", "Accuracy class":"1.6 / 1.0", "Process connection":"1/4\" – 1/2\" NPT/BSP", "Wetted parts":"Copper alloy" } },
  { id:2, name:"Diaphragm Seal Gauge 233.30", brand:"Wika", category:"Pressure Measurement", subcategory:"Diaphragm Seals", leaf:"Threaded Process Connections",
    desc:"Direct-mount diaphragm seal system for viscous, crystallising or corrosive media.",
    specs:{ "Process connection":"Threaded, per DIN/ANSI", "Fill fluid":"Silicone oil", "Diaphragm material":"316L SS" } },
  { id:3, name:"Bimetal Thermometer 55", brand:"Wika", category:"Temperature Measurement", subcategory:"Mechanical Temperature Measurement", leaf:"Bimetallic Thermometers",
    desc:"Rugged, cost-effective local temperature indication for process plant and utilities.",
    specs:{ "Dial size":"100 / 150 mm", "Accuracy class":"Class 1", "Stem length":"63 – 400 mm" } },
  { id:4, name:"RTD Temperature Transmitter T32", brand:"Wika", category:"Temperature Measurement", subcategory:"Electrical Temperature Measurement", leaf:"Temperature Transmitters",
    desc:"Head-mounted 2-wire transmitter, HART-capable, for RTD and thermocouple inputs.",
    specs:{ "Output":"4–20 mA, HART", "Input":"Pt100 / TC", "Housing":"DIN B / Universal" } },
  { id:5, name:"Magnetic Level Gauge NBK", brand:"Trafag", category:"Level Measurement", subcategory:"Mechanical Level Measurement", leaf:"Magnetic Level Gauges",
    desc:"Bypass chamber level indicator with magnetic follower for high-pressure vessels.",
    specs:{ "Max pressure":"up to 420 bar", "Chamber material":"316L SS", "Indicator":"Bi-colour flag / magnetic float" } },
  { id:6, name:"Vibrating Fork Level Switch VF", brand:"ABB", category:"Level Measurement", subcategory:"Level Switches", leaf:"Vibrating Fork Level Switches",
    desc:"Point level detection for liquids, unaffected by turbulence, foam, or bubbles.",
    specs:{ "Output":"Relay / transistor", "Process temp":"-50 to 150 °C", "Approvals":"ATEX / IECEx" } },
  { id:7, name:"Coriolis Mass Flow Meter CFM", brand:"ABB", category:"Flow Measurement", subcategory:"Flow Transmitters", leaf:"Coriolis Mass Flow Meters",
    desc:"Direct mass flow, density and temperature measurement with high turndown ratio.",
    specs:{ "Accuracy":"±0.1% of rate", "Line size":"DN8 – DN150", "Output":"4–20 mA / HART / Modbus" } },
  { id:8, name:"Deadweight Tester CPB3500", brand:"Wika", category:"Calibration Technology", subcategory:"Pressure", leaf:"Precision Pressure Measuring Instruments",
    desc:"Primary pressure standard for calibration laboratories, hydraulic or pneumatic operation.",
    specs:{ "Accuracy":"0.015 – 0.05%", "Range":"up to 3500 bar", "Media":"Oil / Gas" } },
  { id:9, name:"Documenting Process Calibrator", brand:"Trafag", category:"Calibration Technology", subcategory:"Current Voltage Resistance", leaf:"Documenting Multi Function Calibrator",
    desc:"Field calibrator for mA, V, RTD, TC, frequency and pressure with on-board documentation.",
    specs:{ "Accuracy":"0.02% of reading", "Memory":"500+ task records", "Interface":"USB / Bluetooth" } },
  { id:10, name:"Two Valve Manifold", brand:"Mueller", category:"Valves and Fittings", subcategory:"Manifold Valves", leaf:"Two Valve Manifolds",
    desc:"Direct-mount manifold for isolating and equalising pressure/DP transmitters.",
    specs:{ "Max pressure":"6000 – 10000 PSI", "Material":"316 SS / CS", "Connection":"NPT / flanged" } },
  { id:11, name:"Hygienic Butterfly Valve", brand:"Inoxpa", category:"Food and Pharma", subcategory:"Valves", leaf:"Butterfly Valves",
    desc:"Sanitary butterfly valve for food, dairy and pharma process lines.",
    specs:{ "Material":"AISI 316L", "Seat":"EPDM / FDA silicone", "Connection":"Clamp / DIN" } },
  { id:12, name:"High Pressure Regulator HPR", brand:"Alco-Valves", category:"Pressure Regulator", subcategory:"", leaf:"High Pressure Regulator",
    desc:"Single-stage regulator for gas distribution up to high inlet pressures.",
    specs:{ "Inlet pressure":"up to 6000 PSI", "Body material":"316 SS / Brass", "Outlet range":"0–500 PSI" } }
];

/* ---------------- Mega menu build ---------------- */
function buildMegaMenu(){
  const grid = document.getElementById('psMegaGrid');
  const cols = [[],[],[]];
  let i = 0;
  Object.entries(PRODUCT_TAXONOMY).forEach(([cat, subs]) => {
    const col = document.createElement('div');
    col.className = 'ps-mega-col';
    const catLink = document.createElement('a');
    catLink.className = 'ps-cat';
    catLink.href = '#products?category=' + encodeURIComponent(cat);
    catLink.textContent = cat;
    col.appendChild(catLink);
    Object.entries(subs).forEach(([sub, leaves]) => {
      if (sub){
        const subLink = document.createElement('a');
        subLink.className = 'ps-sub';
        subLink.href = '#products?category=' + encodeURIComponent(cat) + '&sub=' + encodeURIComponent(sub);
        subLink.textContent = sub;
        col.appendChild(subLink);
      }
      leaves.forEach(leaf => {
        const leafLink = document.createElement('a');
        leafLink.className = 'ps-leaf';
        leafLink.href = '#products?category=' + encodeURIComponent(cat) + '&sub=' + encodeURIComponent(sub) + '&leaf=' + encodeURIComponent(leaf);
        leafLink.textContent = leaf;
        col.appendChild(leafLink);
      });
    });
    cols[i % 3].push(col);
    i++;
  });
  cols.forEach(colGroup => {
    const wrapper = document.createElement('div');
    wrapper.className = 'ps-mega-col-wrapper';
    colGroup.forEach(c => wrapper.appendChild(c));
    grid.appendChild(wrapper);
  });

  const navItem = document.getElementById('psNavItem');
  const trigger = document.getElementById('psNavTrigger');
  trigger.addEventListener('click', () => {
    navItem.classList.toggle('open');
    trigger.setAttribute('aria-expanded', navItem.classList.contains('open'));
  });
  document.addEventListener('click', (e) => {
    if (!navItem.contains(e.target)) navItem.classList.remove('open');
  });
}

/* ---------------- Filters + grid ---------------- */
const state = { category:'', subcategory:'', brands:new Set() };

function populateCategorySelect(){
  const sel = document.getElementById('psCategory');
  Object.keys(PRODUCT_TAXONOMY).forEach(cat => {
    const opt = document.createElement('option');
    opt.value = cat; opt.textContent = cat;
    sel.appendChild(opt);
  });
  sel.addEventListener('change', () => {
    state.category = sel.value;
    state.subcategory = '';
    populateSubcategorySelect();
    render();
  });
}

function populateSubcategorySelect(){
  const sel = document.getElementById('psSubcategory');
  sel.innerHTML = '<option value="">All Sub Categories</option>';
  if (state.category && PRODUCT_TAXONOMY[state.category]){
    Object.keys(PRODUCT_TAXONOMY[state.category]).forEach(sub => {
      if (!sub) return;
      const opt = document.createElement('option');
      opt.value = sub; opt.textContent = sub;
      sel.appendChild(opt);
    });
  }
  sel.onchange = () => { state.subcategory = sel.value; render(); };
}

function populateBrandList(){
  const list = document.getElementById('psBrandList');
  BRANDS.forEach(brand => {
    const label = document.createElement('label');
    const cb = document.createElement('input');
    cb.type = 'checkbox'; cb.value = brand;
    cb.addEventListener('change', () => {
      cb.checked ? state.brands.add(brand) : state.brands.delete(brand);
      render();
    });
    label.appendChild(cb);
    label.appendChild(document.createTextNode(brand));
    list.appendChild(label);
  });
}

function matchesFilters(p){
  if (state.category && p.category !== state.category) return false;
  if (state.subcategory && p.subcategory !== state.subcategory) return false;
  if (state.brands.size && !state.brands.has(p.brand)) return false;
  return true;
}

function productIcon(){
  return `<svg viewBox="0 0 24 24" fill="none"><rect x="4" y="4" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M8 9h8M8 13h5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>`;
}

function render(){
  const grid = document.getElementById('psGrid');
  const empty = document.getElementById('psEmpty');
  const filtered = PRODUCTS.filter(matchesFilters);
  document.getElementById('psResultCount').textContent = filtered.length;
  grid.innerHTML = '';
  empty.style.display = filtered.length ? 'none' : 'block';
  filtered.forEach(p => {
    const card = document.createElement('div');
    card.className = 'ps-card';
    card.innerHTML = `
      <div class="ps-card-img">${productIcon()}</div>
      <div class="ps-card-body">
        <div class="ps-card-brand">${p.brand}</div>
        <div class="ps-card-title">${p.name}</div>
        <div class="ps-card-cat">${p.subcategory ? p.subcategory + ' — ' : ''}${p.leaf}</div>
        <div class="ps-card-cta">View details →</div>
      </div>`;
    card.addEventListener('click', () => openModal(p));
    grid.appendChild(card);
  });
}

/* ---------------- Product detail modal ---------------- */
function openModal(p){
  document.getElementById('psModalBrand').textContent = p.brand;
  document.getElementById('psModalTitle').textContent = p.name;
  document.getElementById('psModalPath').textContent = [p.category, p.subcategory, p.leaf].filter(Boolean).join(' / ');
  document.getElementById('psModalDesc').textContent = p.desc;
  const specsEl = document.getElementById('psModalSpecs');
  specsEl.innerHTML = Object.entries(p.specs).map(([k,v]) => `<tr><td>${k}</td><td>${v}</td></tr>`).join('');
  document.getElementById('psModalOverlay').classList.add('open');
}
function closeModal(){ document.getElementById('psModalOverlay').classList.remove('open'); }
document.getElementById('psModalClose').addEventListener('click', closeModal);
document.getElementById('psModalOverlay').addEventListener('click', (e) => {
  if (e.target.id === 'psModalOverlay') closeModal();
});
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

document.getElementById('psClear').addEventListener('click', () => {
  state.category = ''; state.subcategory = ''; state.brands.clear();
  document.getElementById('psCategory').value = '';
  populateSubcategorySelect();
  document.querySelectorAll('#psBrandList input').forEach(cb => cb.checked = false);
  render();
});

/* ---------------- init ---------------- */
buildMegaMenu();
populateCategorySelect();
populateSubcategorySelect();
populateBrandList();
render();
