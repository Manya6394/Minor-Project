import './App.css';
import Footer from './User/components/Footer/Footer';
import Navigation from './User/components/Navigation/Navigation';
import HomePage from './User/pages/HomePage/HomePage';

function App() {
  return (
    <div className="App">
      <Navigation/>

      <div>
        <HomePage/>
      </div>

      <Footer/>
    </div>
  );
}

export default App;
