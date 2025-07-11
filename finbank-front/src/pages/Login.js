import styles from '../styles/Login.module.css';
import logo from '../assets/imgs/logofin.png'
function Login() {
    return (
        <div className={styles.container}>
            <div className={styles.card}>
                <div className={styles.imgContainer}>
                    <img src={logo} alt="FinBank Logo" className={styles.logo} />
                </div>
                <form className={styles.form}>
                    <input className={styles.input} type="text" placeholder="Email" />
                    <input className={styles.input} type="password" placeholder="Senha" />
                    <button className={styles.button} type="submit">Entrar</button>
                </form>
            </div>
        </div>
    )
}

export default Login;