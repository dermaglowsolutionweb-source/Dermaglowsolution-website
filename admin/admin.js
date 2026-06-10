import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, doc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyAA0_TNH69s2KoUpFZinEGOVVNlY4JFWpo",
    authDomain: "dermosolution-1dcea.firebaseapp.com",
    projectId: "dermosolution-1dcea",
    storageBucket: "dermosolution-1dcea.firebasestorage.app",
    messagingSenderId: "242600861238",
    appId: "1:242600861238:web:3dd8cb0667deb4163b8297",
    measurementId: "G-9HVNYTH9LZ"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// --- Authentication Logic ---
const ADMIN_USERS = {
    'flyggoagency@gmail.com': 'Flyggo@8',
    'dermaglowsolutionweb@gmail.com': 'Dermaglowsolution@123'
};

// Check Auth state on load
document.addEventListener('DOMContentLoaded', () => {
    const isDashboard = window.location.pathname.includes('dashboard.html');
    const isLoggedIn = localStorage.getItem('admin_logged_in') === 'true';

    if (isDashboard && !isLoggedIn) {
        window.location.href = 'index.html';
    } else if (!isDashboard && isLoggedIn) {
        window.location.href = 'dashboard.html';
    }

    if (isDashboard) {
        initDashboard();
    }
});

// Login Form Handler
const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        if (ADMIN_USERS[email] === password) {
            localStorage.setItem('admin_logged_in', 'true');
            window.location.href = 'dashboard.html';
        } else {
            document.getElementById('errorMsg').style.display = 'block';
        }
    });
}

// Logout Handler
const logoutBtn = document.getElementById('logoutBtn');
if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
        localStorage.removeItem('admin_logged_in');
        window.location.href = 'index.html';
    });
}

// --- Dashboard Logic ---
const PRODUCTS = [
    { name: 'ADSS 4D Tech laser USA FDA 2400w', category: 'ADSS', image: '../images/Adss/2.jpeg' },
    { name: 'ADSS 4D Tech laser', category: 'ADSS', image: '../images/Adss/3.jpeg' },
    { name: 'ADSS 4D Tech laser USA FDA 1600w', category: 'ADSS', image: '../images/Adss/1.jpeg' },
    { name: 'CO2 Laser System', category: 'CO2 Fractional Laser', image: '../images/CO2%20Fractional%20Laser/1.jpeg' },
    { name: 'BV Laser CO2 Metal Tube Technology', category: 'CO2 Fractional Laser', image: '../images/CO2%20Fractional%20Laser/2.jpeg' },
    { name: 'OFA CO2 Fractional Laser', category: 'CO2 Fractional Laser', image: '../images/CO2%20Fractional%20Laser/3.jpeg' },
    { name: 'CO2 Fractional Laser (Rose Gold)', category: 'CO2 Fractional Laser', image: '../images/CO2%20Fractional%20Laser/4.jpeg' },
    { name: 'Q - switched nd yag laser', category: 'Active Pico Laser', image: '../images/Active%20Pico%20Laser/1.jpeg' },
    { name: 'crystal pico laser gear', category: 'Active Pico Laser', image: '../images/Active%20Pico%20Laser/2.jpeg' },
    { name: 'Active Pico Bv Laser', category: 'Active Pico Laser', image: '../images/Active%20Pico%20Laser/3.jpeg' },
    { name: 'q sswitched nd yag laser', category: 'Active Pico Laser', image: '../images/Active%20Pico%20Laser/4.jpeg' },
    { name: 'Q - switched nd yag laser', category: 'Active Pico Laser', image: '../images/ai_adss_1_1780916109986.png' },
    { name: 'Advanced Cryo System', category: 'Cryopilopysis', image: '../images/Cryopilopysis/1.jpeg' },
    { name: 'CRYO Sculpting Machine', category: 'Cryopilopysis', image: '../images/Cryopilopysis/2.jpeg' },
    { name: 'Professional Cryo Device', category: 'Cryopilopysis', image: '../images/Cryopilopysis/3.jpeg' },
    { name: 'Premium Cryolipolysis', category: 'Cryopilopysis', image: '../images/Cryopilopysis/4.jpeg' },

    { name: '8 in 1 alice superbubble max hydra', category: 'Premium Hydra', image: '../images/Premium%20Hydra%20Machines/5.jpeg' },
    { name: '7 in 1 alice super bubble oxygen hydra mechine', category: 'Premium Hydra', image: '../images/ai_hydra_5.png' },
    { name: 'Premium Hydra Device', category: 'Premium Hydra', image: '../images/ai_hydra_6.png' },
        { name: 'Laser Hair Removal System', category: 'Laser hair removal regrowth machine', image: '../images/Laser%20hair%20removal%20regrowth%20machine/1.jpeg' },
    { name: 'Advanced Laser Hair Device', category: 'Laser hair removal regrowth machine', image: '../images/Laser%20hair%20removal%20regrowth%20machine/2.jpeg' },
    { name: 'AI face analyser - Model 1', category: 'AI Face Analyser', image: '../images/ai_face_1_1780916138905.png' },
    { name: 'AI face analyser - Model 2', category: 'AI Face Analyser', image: '../images/ai_face_2_1780916153295.png' },
    { name: 'AI scalp analyzer - Model 1', category: 'AI Scalp Analyzer', image: '../images/ai_scalp_1_1780916166460.png' },
    { name: 'AI scalp analyzer - Model 2', category: 'AI Scalp Analyzer', image: '../images/ai_scalp_2_1780916181425.png' },
    { name: 'EMS SCULPT', category: 'EMS Sculpt', image: '../images/ai_ems_sculpt_1.png' },
    { name: 'EM FACE MACHINE', category: 'EMS Sculpt', image: '../images/ai_ems_sculpt_2.png' },
    { name: 'HIFU - Model 1', category: 'HIFU', image: '../images/ai_hifu_1_1780924655511.png' },
    { name: 'HIFU - Model 2', category: 'HIFU', image: '../images/ai_hifu_2_1780924671247.png' },
    { name: 'HIFU - Model 3', category: 'HIFU', image: '../images/ai_hifu_3_1780924687699.png' },
    { name: '17 IN 1 Hydra Facial Machine', category: 'Premium Hydra', image: '../images/Premium%20Hydra%20Machines/1.jpeg' },
    { name: '17 IN 1 Hydra plus Machine', category: 'Premium Hydra', image: '../images/Premium%20Hydra%20Machines/2.jpeg' },
    { name: '13 in 1 oxygen pdt dynamic hydra', category: 'Premium Hydra', image: '../images/Premium%20Hydra%20Machines/3.jpeg' },
    { name: '10 in 1 oxygen hydra alice superubble', category: 'Premium Hydra', image: '../images/Premium%20Hydra%20Machines/4.jpeg' },
    { name: 'Electric Derma bed - Model 1', category: 'Derma Bed', image: '../images/ai_derma_bed_1_1780924615768.png' },
    { name: 'Electric Derma bed - Model 2', category: 'Derma Bed', image: '../images/ai_derma_bed_2_1780924628217.png' },
    { name: 'Electric Derma bed - Model 3', category: 'Derma Bed', image: '../images/ai_derma_bed_3_1780924641316.png' }
];

window.hiddenProductNames = [];
window.customProductNames = {};

async function initDashboard() {
    try {
        const docRef = doc(db, "settings", "visibility");
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) {
            window.hiddenProductNames = docSnap.data().hiddenProductNames || [];
            window.customProductNames = docSnap.data().customProductNames || {};
        }
    } catch(e) {
        console.error("Firebase read error:", e);
    }
    renderTable();
}

function renderTable() {
    const tbody = document.getElementById('productTableBody');
    if (!tbody) return;
    
    tbody.innerHTML = '';
    
    PRODUCTS.forEach(product => {
        const isHidden = window.hiddenProductNames.includes(product.name);
        const displayName = window.customProductNames[product.name] || product.name;
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>
                <div class="product-cell">
                    <img src="${product.image}" class="product-thumb">
                    <span class="product-name" id="name-${product.name.replace(/\s+/g, '-')}">${displayName}</span>
                    ${displayName !== product.name ? `<small style="display:block;color:#888;font-size:0.75rem;">Original: ${product.name}</small>` : ''}
                </div>
            </td>
            <td style="color: var(--text-muted);">${product.category}</td>
            <td>
                <label class="switch">
                    <input type="checkbox" onchange="window.toggleProduct('${product.name}')" ${!isHidden ? 'checked' : ''}>
                    <span class="slider"></span>
                </label>
            </td>
            <td>
                <span id="status-${product.name.replace(/\s+/g, '-')}" class="status-badge ${isHidden ? 'status-hidden' : 'status-visible'}">
                    ${isHidden ? 'Hidden' : 'Visible'}
                </span>
            </td>
            <td>
                <div class="action-btns">
                    <button class="btn-action" title="Edit Name" onclick="window.editProductName('${product.name.replace(/'/g, "\\'")}')"><i class="fa-solid fa-pen"></i></button>
                </div>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

window.toggleProduct = function(name) {
    if (window.hiddenProductNames.includes(name)) {
        window.hiddenProductNames = window.hiddenProductNames.filter(n => n !== name);
    } else {
        window.hiddenProductNames.push(name);
    }
    
    // Update badge visually
    const isHidden = window.hiddenProductNames.includes(name);
    const badge = document.getElementById(`status-${name.replace(/\s+/g, '-')}`);
    if(badge) {
        badge.className = `status-badge ${isHidden ? 'status-hidden' : 'status-visible'}`;
        badge.innerText = isHidden ? 'Hidden' : 'Visible';
    }
}

window.editProductName = function(originalName) {
    const currentName = window.customProductNames[originalName] || originalName;
    const newName = prompt(`Enter new name for: ${originalName}`, currentName);
    
    if (newName !== null && newName.trim() !== '') {
        window.customProductNames[originalName] = newName.trim();
        renderTable();
    } else if (newName !== null && newName.trim() === '') {
        // If they empty it, revert to original
        delete window.customProductNames[originalName];
        renderTable();
    }
}

// --- Save & Deploy to Firebase ---
const saveBtn = document.getElementById('saveBtn');

if (saveBtn) {
    saveBtn.addEventListener('click', async () => {
        saveBtn.innerText = 'Saving to Database...';
        saveBtn.disabled = true;
        
        try {
            await setDoc(doc(db, "settings", "visibility"), {
                hiddenProductNames: window.hiddenProductNames,
                customProductNames: window.customProductNames
            });
            alert('Settings successfully saved to Firebase Database! The website will now apply these updates instantly.');
        } catch (err) {
            console.error(err);
            alert('Failed to save to database. Make sure your Firestore Security Rules allow read/write access.');
        }
        
        saveBtn.innerHTML = '<i class="fa-solid fa-cloud-arrow-up"></i> Save & Deploy Changes';
        saveBtn.disabled = false;
    });
}
