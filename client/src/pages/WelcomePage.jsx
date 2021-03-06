import styles from '@/styles/WelcomePage.module.css'
import React from 'react'

function WelcomePage() {
  return (
    <div className={styles.base}>
      <div className={styles.small}>Agosto - Noviembre de 2021</div>
      <div className={styles.group}>
        <h2>JOLC</h2>
      </div>
      <div className={styles.group}>
        <h3>¿Qué es Jolc?</h3>
        <ul>
          <li>
            Un intérprete de Jolc, una lenguaje de programación basado en Julia ejecutable
            en la web.
          </li>
          <li>
            Un compilador de Jolc, que genera código intermedio de Go totalmente
            funcional.
          </li>
          <li>
            Un optimizador de código intermedio de Go, a través de optimizaciones locales
            y globales.
          </li>
        </ul>
      </div>
      <div className={styles.group}>
        <h3>Autor</h3>
        <ul>
          <li>
            <a target='blank' href='https://github.com/pabloc54'>
              Pablo Cabrera
            </a>
          </li>
          <li>
            <a target='blank' href='mailto:pablofernando54@outlook.com'>
              pablofernando54@outlook.com
            </a>
          </li>
        </ul>
      </div>
      <div className={styles.group}>
        <h3>Enlaces útiles</h3>
        <ul>
          <li>
            <a target='blank' href='https://julialang.org/'>
              The Julia Programming Language
            </a>
          </li>
          <li>
            <a
              target='blank'
              href='https://www.tutorialspoint.com/julia/julia_basic_syntax.htm'>
              Julia Programming - Basic Syntax
            </a>
          </li>
        </ul>
      </div>
      <div>
        <p>
          Source del proyecto: <a href='https://github.com/pabloc54/jolc'>GitHub</a>
        </p>
      </div>
      <div>
        <p>
          Iconos proporcionados por <a href='https://icons8.com'>Icons8</a>. Créditos a
          sus respectivos autores.
        </p>
      </div>
    </div>
  )
}

export default WelcomePage
