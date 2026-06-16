import { BrowserRouter, Routes, Route } from "react-router-dom";
import ValidationPage from "./pages/ValidationPage";
import QrGenerator from "./pages/QrGenerator";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/validate"
          element={<ValidationPage />}
        />
        <Route path="/" element={<QrGenerator />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;