import { useState } from "react";
import { Link } from "react-router-dom";
import styles from "../styles/Navbar.module.css";

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>FinBank Flow</div>
      
      <button className={styles.toggle} onClick={() => setIsOpen(!isOpen)}>
        ☰
      </button>

      <div className={`${styles.links} ${isOpen ? styles.show : ""}`}>
        <Link to="/" onClick={() => setIsOpen(false)}>Dashboard</Link>
        <Link to="/login" onClick={() => setIsOpen(false)}>Login</Link>
        <Link to="/cadastro" onClick={() => setIsOpen(false)}>Cadastro</Link>
        <Link to="/deposito" onClick={() => setIsOpen(false)}>Depósito</Link>
        <Link to="/pix" onClick={() => setIsOpen(false)}>Pix</Link>
        <Link to="/historico" onClick={() => setIsOpen(false)}>Histórico</Link>
      </div>
    </nav>
  );
}

export default Navbar;
