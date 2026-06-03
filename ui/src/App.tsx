import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import EventTypesPage from './pages/EventTypesPage';
import BookingPage from './pages/BookingPage';
import AdminPage from './pages/AdminPage';

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<EventTypesPage />} />
        <Route path="/book/:eventTypeId" element={<BookingPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
}
