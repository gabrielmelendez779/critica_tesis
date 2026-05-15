# La Matemática de la Inatención: Estabilización e Inercia

Este documento formaliza matemáticamente la "doble cara" de la inatención (*sparsity*) en el modelo DSGE: cómo actúa como ancla estabilizadora ante políticas monetarias laxas, y cómo genera persistencia inercial ante shocks inflacionarios estructurales.

## 1. El Modelo Neokeynesiano Conductual (Sparsity)

Para ilustrar el mecanismo, partimos del modelo Neokeynesiano Conductual basado en Xavier Gabaix (2020), que introduce un parámetro de atención $M \in (0, 1]$. Si $M=1$, el modelo colapsa en el estándar de expectativas racionales. Si $M < 1$, los agentes son "miopes" y descuentan cognitivamente el futuro.

Las dos ecuaciones dinámicas fundamentales del modelo sufren la siguiente modificación estructural:

**1. Curva IS Conductual (Hogares):**
$$ x_t = M_x E_t [x_{t+1}] - \sigma (i_t - E_t [\pi_{t+1}] - r^n_t) $$
Donde $x_t$ es la brecha del producto, $i_t$ la tasa de interés nominal, $\pi_t$ la inflación esperada y $M_x < 1$ es el factor de inatención de los consumidores hacia el futuro macroeconómico.

**2. Curva de Phillips Neokeynesiana Conductual (Empresas):**
$$ \pi_t = \beta M^f E_t [\pi_{t+1}] + \kappa x_t + u_t $$
Donde $M^f < 1$ representa la inatención de las empresas al fijar precios hacia la inflación futura, $\beta$ es el factor de descuento intertemporal, $\kappa$ es la pendiente de la curva (sensibilidad al ciclo) y $u_t$ representa un shock de costos (oferta).

A esto le añadimos una regla de Taylor simplificada para el Banco Central:
$$ i_t = \phi_\pi \pi_t + \phi_x x_t $$

---

## 2. El Lado "Bueno": Estabilización ante Políticas Laxas (Régimen Paloma)

En el modelo tradicional de expectativas racionales ($M_x = M^f = 1$), para que el sistema de ecuaciones en diferencias converja a un equilibrio único y estable (Condiciones de Blanchard-Kahn), el Banco Central debe cumplir estrictamente el **Principio de Taylor**:
$$ \phi_\pi > 1 $$
Es decir, la respuesta a la inflación debe ser mayor a 1 a 1. Si $\phi_\pi < 1$ (Régimen Paloma), el sistema es matemáticamente inestable (raíces explosivas), pues no hay un ancla nominal; cualquier subida en expectativas de inflación baja la tasa real, estimulando el consumo y confirmando la inflación en una espiral infinita.

**¿Qué ocurre al introducir Sparsity ($M < 1$)?**
Al introducir la inatención cognitiva, las raíces del polinomio característico se mueven hacia adentro del círculo unitario. Sustituyendo la Regla de Taylor en el sistema, la nueva condición matemática para la estabilidad (determinancia) se flexibiliza drásticamente a:
$$ \phi_\pi > 1 - \frac{1 - M_x}{\sigma \kappa} $$

Dado que $M_x < 1$, el término $\frac{1 - M_x}{\sigma \kappa}$ es estrictamente positivo. Por lo tanto, el lado derecho de la inecuación se vuelve **estrictamente menor a 1**.

**Conclusión Matemática 1:** El Banco Central puede fijar una respuesta débil $\phi_\pi = 0.80$ y el sistema **seguirá siendo matemáticamente estable**. La miopía de los agentes amortigua la traslación de expectativas futuras al presente, actuando como el ancla que el Banco Central dejó de proveer.

---

## 3. El Lado "Oscuro": Inercia y Persistencia Inflacionaria

Supongamos ahora el escenario inverso: venimos de un estado malo (alta inflación) y el Banco Central adopta una postura "Halcón" ($\phi_\pi \gg 1$) para quebrar la inflación.

Resolviendo la Curva de Phillips conductual hacia adelante (*forward-looking*) iterando sobre expectativas futuras, obtenemos que la inflación hoy es el valor presente descontado de las brechas de producto y shocks futuros:

$$ \pi_t = \sum_{j=0}^{\infty} (\beta M^f)^j E_t [\kappa x_{t+j} + u_{t+j}] $$

**El Problema de la Persistencia (Inercia):**
En un modelo hiper-racional ($M^f = 1$), el factor de descuento es simplemente $\beta^j$. Si el Banco Central anuncia tasas altas para los próximos trimestres, el término $E_t[x_{t+j}]$ (la brecha de producto esperada) se vuelve fuertemente negativo, lo que contrae instantáneamente la sumatoria completa, y la inflación $\pi_t$ cae bruscamente hoy mismo.

Pero con $M^f < 1$, las empresas **descuentan cognitivamente** el esfuerzo futuro del Banco Central. El impacto de una recesión futura ($\kappa x_{t+j}$) pesa mucho menos en sus decisiones de precios de hoy, ya que está castigado por el término $(\beta M^f)^j$, el cual decae hacia cero mucho más velozmente que en el modelo racional.

**Conclusión Matemática 2:** Las empresas inatentas miran poco hacia el futuro de las políticas restrictivas. Su ancla no es la meta del Banco, sino el shock pasado/presente. Para que la ecuación resulte en una misma bajada de $\pi_t$, el Banco Central se ve forzado a infligir un $x_t$ contemporáneo significativamente más negativo (mayor contracción económica). Así, la inatención actúa como una fuerza inercial que hace que **los estados desfavorables persistan mucho más tiempo**.
