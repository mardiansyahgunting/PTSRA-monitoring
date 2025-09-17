import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.lines import Line2D

# =============================================================================
# 1. KONFIGURASI & DATA GRAFIK
# Semua yang perlu Anda ubah ada di sini.
# =============================================================================

# Pengaturan Data
DATA_GRAFIK = {
    "N/A": [("Contracted\nAug '23", 85780, '#0f5257')],
    "Cycle I": [
        ("Ex-ante\nJan '24", 85781, '#b0f2c2'),
        ("PDR\nAug '23-Jan '24", 88015, '#8fdc43'),
        ("MEAS Recorded\nMay '24-Jun '24", 88015, '#585858'),
        ("Validation\nJun '24-Jul '24", (33292, 54723), ('#006d2c', '#ff7c43'))
    ],
    "Cycle I/I": [
        ("Replanting\nFeb '25", 6707, '#7f7f00'),
        ("MEAS Recorded\nFeb '25-Mar '25", 6802, '#585858'),
        ("Validation\nApr '25", 6421, '#006d2c')
    ],
    "Cycle II": [
        ("Ex-ante\n2025", 30012, '#b0f2c2'),
        ("MEAS Recorded\nApr '25-May '25", 13617, '#585858'),
        ("Validation\nJun '25", 13617, '#ff7c43')
    ],
    "Cycle III": [("Ex-ante\n2025", 75125, '#b0f2c2')]
}

# Pengaturan Tampilan Visual
FIG_SIZE = (20, 10)
JARAK_ANTAR_GRUP = 1.5
LEBAR_BAR = 0.8
UKURAN_FONT_LABEL = 12
Y_AXIS_LIMIT = 95000
NAMA_FILE_OUTPUT = "TPP INPROSULA.png"  # Nama file saat gambar disimpan


# =============================================================================
# 2. FUNGSI-FUNGSI PEMBANTU
# =============================================================================

def gambar_batang_grafik(ax, data_grafik):
    """Menggambar semua batang (single & stacked) dan label nilainya."""
    x_pos = 0
    x_ticks_pos = []
    x_tick_labels = []
    cycle_boundaries = []

    for cycle_name, items in data_grafik.items():
        cycle_start_pos = x_pos
        if x_pos > 0:
            ax.axvline(x=x_pos - (JARAK_ANTAR_GRUP / 2), color='gray', linestyle='--', linewidth=0.8)

        for label, value, color in items:
            x_ticks_pos.append(x_pos)
            x_tick_labels.append(label)

            if isinstance(value, tuple):
                bottom_val, top_val = value
                bottom_color, top_color = color
                ax.bar(x_pos, bottom_val, color=bottom_color, width=LEBAR_BAR)
                ax.text(x_pos, bottom_val / 2, f'{bottom_val:,}', ha='center', va='center', color='white',
                        fontsize=UKURAN_FONT_LABEL, fontweight='bold')
                ax.bar(x_pos, top_val, bottom=bottom_val, color=top_color, width=LEBAR_BAR)
                ax.text(x_pos, bottom_val + top_val / 2, f'{top_val:,}', ha='center', va='center', color='white',
                        fontsize=UKURAN_FONT_LABEL, fontweight='bold')
            else:
                ax.bar(x_pos, value, color=color, width=LEBAR_BAR)
                ax.text(x_pos, value + (Y_AXIS_LIMIT * 0.01), f'{value:,}', ha='center', va='bottom', color='black',
                        fontsize=UKURAN_FONT_LABEL)

            x_pos += 1

        cycle_boundaries.append({'label': cycle_name, 'start': cycle_start_pos, 'end': x_pos - 1})
        x_pos += (JARAK_ANTAR_GRUP - 1)

    return x_ticks_pos, x_tick_labels, cycle_boundaries


def atur_tampilan_plot(ax, x_ticks_pos, x_tick_labels, cycle_boundaries):
    """Mengatur judul, label sumbu, grid, dan elemen visual lainnya."""
    fig = ax.figure
    fig.suptitle('TPP INPROSULA', fontsize=20, y=1.02, fontweight='bold')
    ax.set_title(
        'Trees Overview by Cycle\nPDR: Purchased-Distributed-Received, MEAS: Measurements',
        fontsize=12, pad=20
    )

    ax.set_xticks(x_ticks_pos)
    ax.set_xticklabels(
        x_tick_labels,
        fontsize=11,
        rotation=30,  # Memutar label agar tidak bertabrakan
        ha='right'  # Mengatur posisi horizontal label yang diputar
    )
    ax.set_ylim(0, Y_AXIS_LIMIT)
    ax.set_ylabel('Measure Value', fontsize=12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f'{int(y / 1000)}K'))

    ax.grid(axis='y', linestyle='-', alpha=0.5)
    ax.tick_params(axis='x', length=0)
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)

    for boundary in cycle_boundaries:
        center_pos = (boundary['start'] + boundary['end']) / 2
        ax.text(center_pos, ax.get_ylim()[1] * 1.02, boundary['label'], ha='center', va='bottom', fontsize=12,
                fontweight='bold')


def buat_legenda(ax):
    """Membuat dan menempatkan legenda kustom di sebelah kanan grafik."""
    legend_elements = [
        Line2D([0], [0], color='#0f5257', lw=6, label='Contracted, --'),
        Line2D([0], [0], color='#b0f2c2', lw=6, label='Ex-ante, --'),
        Line2D([0], [0], color='#8fdc43', lw=6, label='PDR, --'),
        Line2D([0], [0], color='#585858', lw=6, label='MEAS Recorded,...'),
        Line2D([0], [0], color='#ff7c43', lw=6, label='Validation, Reje...'),
        Line2D([0], [0], color='#006d2c', lw=6, label='Validation, Appr...'),
        Line2D([0], [0], color='#7f7f00', lw=6, label='Replanting, --')
    ]
    ax.legend(
        handles=legend_elements, title='Measure Type, Vali...',
        loc='upper left', bbox_to_anchor=(1.01, 1),
        fontsize=11, title_fontsize=12
    )


# =============================================================================
# 3. ALUR UTAMA EKSEKUSI
# =============================================================================

if __name__ == "__main__":
    # 1. Siapkan kanvas plot
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    # 2. Gambar semua data batang ke kanvas
    x_ticks_pos, x_tick_labels, cycle_boundaries = gambar_batang_grafik(ax, DATA_GRAFIK)

    # 3. Atur semua elemen visual (judul, sumbu, grid, dll.)
    atur_tampilan_plot(ax, x_ticks_pos, x_tick_labels, cycle_boundaries)

    # 4. Tambahkan legenda
    buat_legenda(ax)

    # 5. Rapikan layout
    plt.tight_layout(rect=[0, 0, 0.85, 0.9])

    # 6. Simpan gambar ke file
    plt.savefig(NAMA_FILE_OUTPUT, dpi=300, bbox_inches='tight')

    # 7. Tampilkan hasil akhir
    plt.show()

print(f"Grafik telah berhasil dibuat dan disimpan sebagai '{NAMA_FILE_OUTPUT}'")