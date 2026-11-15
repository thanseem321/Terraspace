
from database import create_table, get_connection

sites = [
    (
        "LRO-01",
        "Lonar Crater, Maharashtra, India",
        "Moon",
        "Lunar Maria Basalt Craters",
        19.976, 76.508,
        "Hyper-velocity Basaltic Impact Crater",
        "92%",
        "Formed in Deccan basaltic rock, mirroring lunar mare impact craters in mineralogy and ejecta structure.",
        "Crater wall rover traversal, basaltic regolith drilling, and impact geology.",
        "NASA LRO LOLA Elevation & LROC Imagery (PDS)",
        "https://nasa.gov"
    ),
    (
        "LRO-02",
        "Haughton Crater, Devon Island, Canada",
        "Moon",
        "Shackleton Crater (Lunar South Pole)",
        75.43, -89.68,
        "Polar Impact Crater & Permafrost",
        "95%",
        "Sub-zero temperatures, rocky impact breccia, and low-angle polar sunlight mirror Artemis Lunar South Pole landing zones.",
        "Pressurized rover operations, spacesuit mobility, and subsurface ice extraction.",
        "NASA LRO Diviner Lunar Radiometer & LOLA Polar Data",
        "https://nasa.gov"
    ),
    (
        "LRO-03",
        "Craters of the Moon, Idaho, USA",
        "Moon",
        "Marius Hills Lunar Skylights",
        43.41, -113.51,
        "Basaltic Lava Flows & Subsurface Lava Tubes",
        "90%",
        "Intact volcanic lava tubes provide natural shielding against cosmic radiation and micrometeorites.",
        "Autonomous cave mapping drones and permanent underground lunar habitat modules.",
        "NASA GRAIL Gravity Data & LRO Terrain Camera",
        "https://nasa.gov"
    ),
    (
        "LRO-04",
        "Mauna Loa / PISCES, Hawaii, USA",
        "Moon",
        "Lunar Highlands & Mare Regolith",
        19.47, -155.60,
        "Fine Basaltic Tephra & Volcanic Ash",
        "94%",
        "Glass-rich volcanic ash closely replicates abrasive, electrostatically charged lunar dust.",
        "In-Situ Resource Utilization (ISRU), robotic landing pad sintering, and dust seals.",
        "NASA Artemis Lunar Regolith Simulant & LRO Spectral Profiles",
        "https://nasa.gov"
    ),
    (
        "MRO-01",
        "Tso Kar & Ladakh, India",
        "Mars",
        "Jezero Crater & Martian Paleolakes",
        33.30, 78.00,
        "High-Altitude Cold Desert & Evaporite Salt Flats",
        "91%",
        "Thin dry atmosphere, high UV radiation, and saline permafrost mirror ancient Martian lakebeds.",
        "Astrobiology biosignature detection, extreme cold habitat insulation, and rover endurance.",
        "NASA MRO CRISM Mineralogy & NASA Earthdata",
        "https://nasa.gov"
    ),
    (
        "MRO-02",
        "Atacama Desert, Chile",
        "Mars",
        "Gale Crater & Elysium Planitia",
        -24.50, -69.25,
        "Hyper-Arid Perchlorate Desert",
        "96%",
        "Near-zero rainfall, intense UV flux, and perchlorate-rich soils match Martian surface chemistry.",
        "Autonomous life-detection rovers and deep subsurface regolith drills.",
        "NASA Curiosity SAM & MRO HiRISE Imagery",
        "https://nasa.gov"
    )
]

def insert_sites():
    create_table()
    conn = get_connection()

    conn.executemany("""
        INSERT OR REPLACE INTO sites
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sites)

    conn.commit()
    conn.close()

    print("TerraSpace database initialized successfully!")
    print("6 locations inserted.")

if __name__ == "__main__":
    insert_sites()
