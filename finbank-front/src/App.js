import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from './pages/Home';
import Cadastro from './pages/Cadastro'
import Deposito from './pages/Deposito';
import Historico from './pages/Historico';
import Pix from './pages/Pix';
import Login from './pages/Login';
import Navbar from './components/Navbar';

import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/cadastro" element={<Cadastro />} />
        <Route path="/login" element={<Login />} />
        <Route path="/deposito" element={<Deposito />} />
        <Route path="/historico" element={<Historico />} />
        <Route path="/pix" element={<Pix />} />
      </Routes>
    </Router>

  );
}

export default App;
