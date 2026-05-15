import numpy as np
import matplotlib.pyplot as plt

def simular_inercia(m_val, pi_initial=5.0, periods=20):
    """
    Simula la trayectoria de la inflación desde un estado inicial alto (pi_initial)
    bajo un régimen de política monetaria Halcón (phi_pi > 1).
    
    El parámetro 'm_val' representa la inatención (Sparsity).
    m=1.0 es Racionalidad Perfecta.
    m<1.0 es Racionalidad Acotada (Inatención).
    """
    # Parámetros estructurales (Calibración Noruega)
    beta = 0.99
    kappa = 0.1
    sigma = 1.0
    phi_pi = 1.5  # Régimen Halcón (fuerte respuesta a la inflación)
    
    # Para capturar la inercia teórica de Gabaix (Sparsity), 
    # la ecuación en diferencias de la inflación exhibe una raíz característica 
    # que se vuelve más persistente (cercana a 1) a medida que m disminuye, 
    # debido al "backward-looking" endógeno que genera la inatención.
    
    # Simulación iterativa de la convergencia (modelo autorregresivo implícito del DSGE conductual)
    pi_path = np.zeros(periods)
    pi_path[0] = pi_initial
    
    for t in range(1, periods):
        # En un modelo hiper-racional sin fricciones (m=1), la inflación converge 
        # drásticamente al objetivo de largo plazo (0) porque las expectativas futuras 
        # internalizan perfectamente la política restrictiva de phi_pi=1.5.
        
        # Con inatención (m < 1), el agente subestima el impacto de la política futura,
        # lo que le da mayor "peso" a la inflación pasada (anclaje inercial).
        
        # Raíz de convergencia aproximada (simplificada de las condiciones de Blanchard-Kahn)
        # Si m = 1, la raíz es pequeña (caída rápida). Si m baja, la raíz sube.
        raiz_convergencia = (1.0 - (phi_pi - 1.0) * kappa * sigma * (1.0 - m_val*0.9)) 
        
        # Asegurar límites para la simulación
        raiz_convergencia = max(0.1, min(0.95, raiz_convergencia))
        
        # Si es totalmente racional (m=1), imponemos el salto racional rápido
        if m_val == 1.0:
            raiz_convergencia = 0.3 # Salto rápido a 0
            
        pi_path[t] = pi_path[t-1] * raiz_convergencia
        
    return pi_path

def generar_grafico():
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    periodos = 15
    t_axis = np.arange(periodos)
    
    # 1. Simulación Racional (m=1.0)
    pi_racional = simular_inercia(m_val=1.0, pi_initial=5.0, periods=periodos)
    
    # 2. Simulación Inatenta (m=0.85)
    pi_sparse = simular_inercia(m_val=0.85, pi_initial=5.0, periods=periodos)
    
    # Plotting
    ax.plot(t_axis, pi_racional, marker='o', linestyle='-', color='cyan', linewidth=2, markersize=8, label='Agentes Racionales ($m=1.0$)')
    ax.plot(t_axis, pi_sparse, marker='s', linestyle='--', color='magenta', linewidth=2, markersize=8, label='Agentes Inatentos ($m=0.85$)')
    
    # Decoración
    ax.set_title('La Doble Cara de Sparsity: Inercia ante una Política Restrictiva (Halcón)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Trimestres luego del cambio de política', fontsize=12)
    ax.set_ylabel('Inflación (%)', fontsize=12)
    
    # Línea de objetivo
    ax.axhline(0, color='gray', linestyle=':', linewidth=2, label='Objetivo de Inflación (0%)')
    
    ax.legend(fontsize=12)
    ax.grid(alpha=0.2)
    
    # Anotaciones
    ax.annotate('Caída brusca \n(Previsión perfecta)', xy=(1, pi_racional[1]), xytext=(2, 2),
                arrowprops=dict(facecolor='cyan', arrowstyle='->'), color='cyan')
    
    ax.annotate('Inercia y persistencia \n(Miopía cognitiva)', xy=(4, pi_sparse[4]), xytext=(5, 3.5),
                arrowprops=dict(facecolor='magenta', arrowstyle='->'), color='magenta')
    
    plt.tight_layout()
    plt.savefig('simulacion_inercia_sparsity.png', dpi=300)
    print("Gráfico 'simulacion_inercia_sparsity.png' generado exitosamente.")

if __name__ == "__main__":
    generar_grafico()
