import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

def analizar_produccion(filepath):
    # 1. Carga de datos
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    series_name = df.columns[0]
    df.columns = ['IP_Index']
    
    # 2. Transformaciones Cruciales para DSGE
    # a) Tasa de crecimiento YoY (%)
    df['Growth_YoY'] = df['IP_Index'].pct_change(periods=12) * 100
    
    # b) Output Gap (Ciclo HP sobre el log de la serie)
    log_ip = np.log(df['IP_Index'].dropna())
    # lambda = 14400 para datos mensuales
    cycle, trend = sm.tsa.filters.hpfilter(log_ip, lamb=14400)
    df['OutputGap'] = cycle * 100 # Multiplicamos por 100 para tener porcentaje de desviación
    
    print("="*60)
    print(f"ANÁLISIS DESCRIPTIVO: PRODUCCIÓN INDUSTRIAL NORUEGA ({series_name})")
    print("="*60)
    
    # 3. Estadísticas Descriptivas (del Crecimiento y del Gap)
    print("\nResumen Estadístico (Crecimiento YoY %):")
    print(df['Growth_YoY'].describe())
    
    print("\nResumen Estadístico (Output Gap %):")
    print(df['OutputGap'].describe())
    
    # 4. Visualización
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 12))
    
    # Subplot 1: Índice y Tendencia
    ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2)
    ax1.plot(df.index, df['IP_Index'], color='gray', alpha=0.5, label='Índice Original')
    ax1.plot(df.index, np.exp(trend), color='lime', linewidth=2, label='Tendencia (HP Filter)')
    ax1.set_title('Índice de Producción Industrial y Tendencia Estructural', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.2)
    
    # Subplot 2: Output Gap (El motor del DSGE)
    ax2 = plt.subplot2grid((3, 2), (1, 0), colspan=2)
    ax2.fill_between(df.index, df['OutputGap'], 0, where=(df['OutputGap'] >= 0), color='lime', alpha=0.3, label='Gap Positivo')
    ax2.fill_between(df.index, df['OutputGap'], 0, where=(df['OutputGap'] < 0), color='red', alpha=0.3, label='Gap Negativo')
    ax2.plot(df.index, df['OutputGap'], color='white', linewidth=1)
    ax2.set_title('Output Gap ($x_t$): Desviaciones respecto a la Tendencia (%)', fontsize=14)
    ax2.axhline(y=0, color='white', linestyle='-', alpha=0.5)
    ax2.legend()
    ax2.grid(True, alpha=0.2)
    
    # Subplot 3: Histograma del Gap
    ax3 = plt.subplot2grid((3, 2), (2, 0))
    df['OutputGap'].hist(bins=40, ax=ax3, color='cyan', alpha=0.6)
    ax3.set_title('Distribución del Output Gap', fontsize=12)
    
    # Subplot 4: Volatilidad Móvil del Crecimiento
    ax4 = plt.subplot2grid((3, 2), (2, 1))
    df['Growth_YoY'].rolling(12).std().plot(ax=ax4, color='orange')
    ax4.set_title('Incertidumbre en la Actividad (Std Dev 12m)', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('analisis_produccion.png', dpi=300)
    print("\n[+] Gráficas generadas y guardadas como 'analisis_produccion.png'")
    
    # 5. Persistencia del Ciclo
    acf = sm.tsa.acf(df['OutputGap'].dropna(), nlags=12)
    print(f"\nPersistencia del Output Gap (rho_x): {acf[1]:.4f}")
    
    return df

if __name__ == "__main__":
    analizar_produccion('NORPRINTO01IXOBM.csv')
