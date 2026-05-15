# Análisis de Cambio Estructural en Política Monetaria (Noruega)
## Modelo: NK-DSGE con Sparsity y Markov Switching

### 1. Agentes y Racionalidad Acotada (Sparsity)
Siguiendo a **Gabaix (2020)**, los agentes no son plenamente racionales. Optimizan sujetos a un sesgo cognitivo donde el operador de expectativas $E_t$ se ve atenuado por un parámetro de atención $m \in [0, 1]$.

- **Curva IS Miopizada:**
  $$y_t = m E_t[y_{t+1}] - \sigma^{-1}(i_t - m E_t[\pi_{t+1}] - r_t^n)$$
- **Curva de Phillips (PC) con Desatención:**
  $$\pi_t = \beta m E_t[\pi_{t+1}] + \kappa y_t + \epsilon_{\pi,t}$$

### 2. Política Monetaria (Markov Switching)
El Banco Central de Noruega ajusta la tasa de interés nominal $i_t$ siguiendo una Regla de Taylor cuyos parámetros dependen del estado $S_t$:

$$i_t = \rho(S_t) i_{t-1} + (1-\rho(S_t)) [\phi_\pi(S_t) \pi_t + \phi_y(S_t) y_t] + \epsilon_{i,t}$$

- **Régimen 1 (Post-2001):** Alta reacción a la inflación ($\phi_\pi > 1$).
- **Régimen 2 (Crisis/Pre-2001):** Reacción débil o enfoque en producto ($\phi_\pi < 1$).

### 3. Solución del Sistema
El modelo se resuelve como un sistema de ecuaciones de diferencia estocásticas acopladas. La solución toma la forma de una regla de decisión lineal para cada régimen:
$$X_t = T(S_t) X_{t-1} + R(S_t) \epsilon_t$$

Donde $X_t = [y_t, \pi_t, i_t]'$. La matriz $T(S_t)$ se obtiene mediante un algoritmo de punto fijo que considera tanto la miopía de los agentes ($m$) como las probabilidades de transición entre estados de la política monetaria.

### 4. Ventajas del Enfoque
1. **Inercia Realista:** La Sparsity explica por qué la inflación noruega no reacciona instantáneamente a los anuncios (rompe el *Forward Guidance Puzzle*).
2. **Cambio Estructural:** El Markov Switching permite identificar empíricamente cuándo el Norges Bank cambió su postura ante choques externos (petróleo).
3. **Estabilidad:** El modelo permite periodos transitorios de política "pasiva" sin violar la estabilidad macroeconómica global.

markdown_content = """# Propuesta de Tesis: Cambio Estructural en Noruega con Sparsity y MS

Este documento resume la estructura técnica y bibliográfica para el análisis de la política monetaria noruega, integrando **Markov Switching (MS)** y **Racionalidad Acotada (Sparsity)**.

## 1. El Núcleo del Modelo: New Keynesian Sparsity (Gabaix, 2020)

Se abandona el modelo CIA (Cash-in-Advance) por un modelo Neokeynesiano donde los agentes son "miopes" o desatentos.

### Ecuaciones de Comportamiento:
- **IS Esparsa:** $y_t = m E_t[y_{t+1}] - \\sigma^{-1}(i_t - m E_t[\\pi_{t+1}] - r_t^n)$
- **Phillips (NKPC) Esparsa:** $\\pi_t = \\beta m E_t[\\pi_{t+1}] + \\kappa y_t + \\epsilon_{\\pi,t}$

*Donde $m < 1$ representa el grado de atención (Sparsity). Si $m=1$, volvemos a expectativas racionales.*

## 2. Política Monetaria: Markov Switching (MS)

La Regla de Taylor para Noruega incluye una reacción al tipo de cambio y parámetros que cambian según el régimen $S_t$:

$$i_t = \\rho(S_t) i_{t-1} + (1-\\rho(S_t)) [ \\phi_\\pi(S_t) \\pi_t + \\phi_y(S_t) y_t + \\phi_e(S_t) \\Delta e_t ] + \\epsilon_{i,t}$$

- **Régimen Activo:** Reacción agresiva a la inflación ($\\phi_\\pi > 1.5$).
- **Régimen Pasivo:** Reacción débil, común en crisis o transición energética ($\\phi_\\pi < 1$).

## 3. Bibliografía Estratégica

### Pilares Teóricos
- **Gabaix, X. (2020).** *A Behavioral New Keynesian Model*. AER. [https://doi.org/10.1257/aer.20161483](https://doi.org/10.1257/aer.20161483)
- **Farmer, R. E., Waggoner, D. F., & Zha, T. (2011).** *Minimal State Variable Solutions to MS-DSGE*. JEDC. [https://doi.org/10.1016/j.jedc.2011.08.004](https://doi.org/10.1016/j.jedc.2011.08.004)
- **Davig, T., & Leeper, E. M. (2007).** *Generalizing the Taylor Principle*. AER. [https://doi.org/10.1257/aer.97.3.607](https://doi.org/10.1257/aer.97.3.607)

### Contexto Noruego
- **Bjørnland, H. C., & Halvorsen, J. S. (2014).** *How Does Monetary Policy Respond to Exchange Rate Movements?*. OBES. [https://doi.org/10.1111/obes.12030](https://doi.org/10.1111/obes.12030)
- **Gerdrup, K. R., et al. (2017).** *The Importance of Policy Expectations for the Forward Guidance Puzzle*. Norges Bank WP. [Link](https://www.norges-bank.no/en/news-publications/Publications/Working-Papers/2017/122017/)

## 4. Código de Solución (Python Snippet)

```python
# Implementación básica del solver de punto fijo para T(S_t)
import numpy as np

def solve_ms_sparsity(m, P, params):
    # A_s * X_t = B_s * X_{t-1} + C_s * m * E_t[X_{t+1}]
    # Algoritmo de punto fijo para hallar matrices de política T[s]
    pass # (Ver implementación completa en historial)