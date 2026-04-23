import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

def analizar_interes(filepath):
    # 1. Carga de datos
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    series_name = df.columns[0]
    df.columns = ['InterestRate']
    
    print("="*60)
    print(f"ANÁLISIS DESCRIPTIVO: TASA DE INTERÉS NORUEGA ({series_name})")
    print("="*60)
    
    # 2. Estadísticas Descriptivas
    stats = df['InterestRate'].describe()
    print("\nResumen Estadístico:")
    print(stats)
    print(f"Sesgo (Skewness): {df['InterestRate'].skew():.4f}")
    print(f"Curtosis: {df['InterestRate'].kurtosis():.4f}")
    
    # 3. Visualización
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 10))
    
    # Subplot 1: Serie Temporal
    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
    ax1.plot(df.index, df['InterestRate'], color='#f06292', linewidth=2, label='Tasa 3-Meses (%)')
    ax1.axhline(y=df['InterestRate'].mean(), color='white', linestyle='--', alpha=0.5, label=f'Media: {df["InterestRate"].mean():.2f}%')
    ax1.set_title('Evolución de la Tasa de Interés en Noruega (Interbank 3M)', fontsize=14, color='white')
    ax1.set_ylabel('Tasa Nominal (%)')
    ax1.legend()
    ax1.grid(True, alpha=0.2)
    
    # Subplot 2: Histograma y Densidad
    ax2 = plt.subplot2grid((2, 2), (1, 0))
    df['InterestRate'].hist(bins=30, ax=ax2, color='#f06292', alpha=0.6, density=True)
    df['InterestRate'].plot(kind='kde', ax=ax2, color='white', linewidth=2)
    ax2.set_title('Distribución de Frecuencias (Tasas)', fontsize=12)
    ax2.grid(True, alpha=0.2)
    
    # Subplot 3: Spread de Volatilidad (Rolling Std Dev)
    ax3 = plt.subplot2grid((2, 2), (1, 1))
    rolling_std = df['InterestRate'].rolling(window=12).std()
    ax3.plot(rolling_std, color='yellow', label='Volatilidad Móvil (12m)')
    ax3.set_title('Incertidumbre de Política Monetaria (Std Dev 12m)', fontsize=12)
    ax3.fill_between(rolling_std.index, rolling_std, color='yellow', alpha=0.1)
    ax3.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('analisis_interes.png', dpi=300)
    print("\n[+] Gráficas generadas y guardadas como 'analisis_interes.png'")
    
    # 4. Análisis de Persistencia
    acf = sm.tsa.acf(df['InterestRate'], nlags=12)
    print(f"\nPersistencia (rho): {acf[1]:.4f}")
    
    # 5. Conclusiones para el Problema
    print("\nDiagnóstico de Política Monetaria:")
    if df['InterestRate'].min() < 0.5:
        print("-> Riesgo de ZLB (Zero Lower Bound): Tasas cercanas a cero detectadas.")
    
    if stats['std'] > 2:
        print("-> Alta reactividad: El Banco Central ha realizado ajustes agresivos históricamente.")

    return df

if __name__ == "__main__":
    analizar_interes('IR3TIB01NOM156N.csv')
