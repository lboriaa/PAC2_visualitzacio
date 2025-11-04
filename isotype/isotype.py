import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# --- Carregar dades ---
df = pd.read_csv(
    "https://ourworldindata.org/grapher/share-of-women-in-parliament.csv?v=1&csvType=full&useColumnShortNames=true",
    storage_options={'User-Agent': 'Our World In Data data fetch/1.0'}
)

year = 2024
paises = ["Sweden", "Spain", "United Kingdom", "France", "Italy", "United States", "Japan"]

df_filtered = df[
    (df["Year"] == year) &
    (df["Entity"].isin(paises)) &
    (df["wom_parl_vdem__estimate_best"].notna())
]

if df_filtered.empty:
    print(f"No hi ha dades disponibles per l'any {year}.")
else:
    df_filtered = df_filtered.sort_values("wom_parl_vdem__estimate_best", ascending=False)
    countries = df_filtered["Entity"].tolist()
    share_women = df_filtered["wom_parl_vdem__estimate_best"].tolist()

    # --- Carregar icons ---
    woman_icon = mpimg.imread("woman.png")
    man_icon = mpimg.imread("man.png")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis("off")
    ax.set_title(f"Dones en el Parlament ({year})\n(1 icono = 10%)", fontsize=14, pad=25, weight="bold")

    # --- Dibuixar els isotypes ---
    for i, (country, women_share) in enumerate(zip(countries, share_women)):
        women_icons = int(round(women_share / 10))
        men_icons = 10 - women_icons

        # Dibuixar cada icon amb una separació més amplia
        for j in range(10):
            icon = woman_icon if j < women_icons else man_icon
            imagebox = OffsetImage(icon, zoom=0.07, alpha=0.95)
            ab = AnnotationBbox(imagebox, (j * 1.1, -i), frameon=False)
            ax.add_artist(ab)

        # Etiquetes país i percentatge
        ax.text(-1.5, -i, country, va="center", ha="right", fontsize=12, fontweight="bold")
        ax.text(11.5, -i, f"{women_share:.1f}%", va="center", ha="left", fontsize=11)

    # --- Ajustar marges i límits ---
    ax.set_xlim(-3, 13)
    ax.set_ylim(-len(countries) + 0.5, 1)
    plt.subplots_adjust(left=0.2, right=0.9, top=0.85, bottom=0.05)
    plt.show()
    plt.savefig("isotype.png")