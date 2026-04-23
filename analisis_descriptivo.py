import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

def analizar_inflacion(filepath):
    # 1. Carga de datos
    # FRED CSVs suelen tener 'DATE' y el valor de la serie
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    series_name = df.columns[0]
    df.columns = ['Inflation']
    
    print("="*60)
    print(f"ANÁLISIS DESCRIPTIVO: INFLACIÓN NORUEGA ({series_name})")
    print("="*60)
    
    # 2. Estadísticas Descriptivas
    stats = df['Inflation'].describe()
    print("\nResumen Estadístico:")
    print(stats)
    print(f"Sesgo (Skewness): {df['Inflation'].skew():.4f}")
    print(f"Curtosis: {df['Inflation'].kurtosis():.4f}")
    
    # 3. Visualización
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 10))
    
    # Subplot 1: Serie Temporal
    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
    ax1.plot(df.index, df['Inflation'], color='cyan', linewidth=1.5, label='Inflación YoY %')
    ax1.axhline(y=df['Inflation'].mean(), color='red', linestyle='--', alpha=0.7, label=f'Media: {df["Inflation"].mean():.2f}%')
    ax1.set_title('Evolución de la Inflación en Noruega (YoY)', fontsize=14, color='white')
    ax1.set_ylabel('% Crecimiento')
    ax1.legend()
    ax1.grid(True, alpha=0.2)
    
    # Subplot 2: Histograma y Densidad
    ax2 = plt.subplot2grid((2, 2), (1, 0))
    df['Inflation'].hist(bins=30, ax=ax2, color='lime', alpha=0.6, density=True)
    df['Inflation'].plot(kind='kde', ax=ax2, color='white', linewidth=2)
    ax2.set_title('Distribución de Frecuencias', fontsize=12)
    ax2.grid(True, alpha=0.2)
    
    # Subplot 3: Volatilidad Móvil (Desviación estándar de 12 meses)
    ax3 = plt.subplot2grid((2, 2), (1, 1))
    rolling_std = df['Inflation'].rolling(window=12).std()
    ax3.plot(rolling_std, color='orange', label='Volatilidad Móvil (12m)')
    ax3.set_title('Volatilidad de la Inflación (Std Dev 12m)', fontsize=12)
    ax3.fill_between(rolling_std.index, rolling_std, color='orange', alpha=0.2)
    ax3.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('analisis_inflacion.png', dpi=300)
    print("\n[+] Gráficas generadas y guardadas como 'analisis_inflacion.png'")
    
    # 4. Análisis de Autocorrelación (Persistencia)
    print("\nAnálisis de Persistencia:")
    acf = sm.tsa.acf(df['Inflation'], nlags=12)
    print(f"Autocorrelación Lag-1 (rho): {acf[1]:.4f}")
    if acf[1] > 0.8:
        print("-> Alta persistencia: La inflación tiende a autoperpetuarse (inercia inflacionaria).")
    
    # 5. Detección de Cambios de Régimen (Simple)
    # Si la inflación reciente es muy superior a la media histórica
    media_historica = df['Inflation'].mean()
    ultima_inflacion = df['Inflation'].iloc[-1]
    print(f"\nEstado Actual:")
    print(f"Último dato: {ultima_inflacion:.2f}% | Media Histórica: {media_historica:.2f}%")
    
    if ultima_inflacion > media_historica + stats['std']:
        print("(!) ADVERTENCIA: La inflación actual está significativamente por encima de su tendencia histórica.")
    
    return df

if __name__ == "__main__":
    analizar_inflacion('CPGREN01NOM659N.csv')
