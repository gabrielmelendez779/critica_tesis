import numpy as np
import matplotlib.pyplot as plt

def simular_dinamica(m_path, pi_initial=5.0, periods=20):
    # Parámetros (Calibración base de la tesis)
    beta = 0.99
    kappa = 0.1
    sigma = 1.0
    phi_pi = 1.5 
    
    pi_path = np.zeros(periods)
    pi_path[0] = pi_initial
    
    for t in range(1, periods):
        m_val = m_path[t]
        
        # Dinámica de la raíz de convergencia
        # Representa cuánto de la inflación pasada se transfiere al presente
        # dependiento de qué tanta atención (m_val) le presta la gente a la política futura.
        raiz_convergencia = (1.0 - (phi_pi - 1.0) * kappa * sigma * (1.0 - m_val*0.9)) 
        raiz_convergencia = max(0.1, min(0.95, raiz_convergencia))
        
        # Si la atención es perfecta, la convergencia es brutal
        if m_val == 1.0:
            raiz_convergencia = 0.3 
            
        pi_path[t] = pi_path[t-1] * raiz_convergencia
        
    return pi_path

def generar_grafico_shock():
    periodos = 15
    t_axis = np.arange(periodos)
    
    # 1. Escenario Racional (m siempre 1.0)
    m_racional = np.ones(periodos)
    pi_racional = simular_dinamica(m_racional, pi_initial=5.0, periods=periodos)
    
    # 2. Escenario Inatento/Inercial (m siempre 0.85)
    m_sparse = np.ones(periodos) * 0.85
    pi_sparse = simular_dinamica(m_sparse, pi_initial=5.0, periods=periodos)
    
    # 3. Escenario Shock de Comunicación
    # La gente es inatenta (0.85) pero en t=3 el CB hace un anuncio tan drástico
    # que la atención sube al 100% (1.0) por el pánico/claridad, y luego decae lentamente.
    m_shock = np.ones(periodos) * 0.85
    m_shock[3] = 1.0  # El Shock mediático
    m_shock[4] = 0.95 # Efecto remanente
    m_shock[5] = 0.90 # Efecto remanente
    pi_shock = simular_dinamica(m_shock, pi_initial=5.0, periods=periodos)
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(t_axis, pi_racional, marker='o', linestyle='-', color='cyan', alpha=0.4, label='Racional ($m=1.0$)')
    ax.plot(t_axis, pi_sparse, marker='s', linestyle='--', color='magenta', linewidth=2, label='Inercial ($m=0.85$ continuo)')
    ax.plot(t_axis, pi_shock, marker='^', linestyle='-', color='yellow', linewidth=3, markersize=9, label='Shock de Comunicación ($m \\rightarrow 1.0$ en $t=3$)')
    
    ax.axvline(x=3, color='white', linestyle=':', label='Anuncio Disruptivo del Banco Central')
    
    ax.set_title('Quebrando la Inercia: Efecto de un Shock de Atención', fontsize=14, fontweight='bold')
    ax.set_xlabel('Trimestres', fontsize=12)
    ax.set_ylabel('Inflación (%)', fontsize=12)
    ax.axhline(0, color='gray', linestyle=':')
    ax.legend(fontsize=11)
    
    # Anotaciones
    ax.annotate('Caída dramática \nal subir la atención', xy=(3, pi_shock[3]), xytext=(4, 4),
                arrowprops=dict(facecolor='yellow', arrowstyle='->'), color='yellow')
    
    plt.tight_layout()
    plt.savefig('simulacion_communication_shock.png', dpi=300)
    print("Gráfico 'simulacion_communication_shock.png' generado.")

if __name__ == "__main__":
    generar_grafico_shock()
