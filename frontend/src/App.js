// routes
import Router from './routes';
// theme
import ThemeProvider from './theme';
// components
import ScrollToTop from './components/scroll-to-top';
import { StyledChart } from './components/chart';
import { AuthProvider } from './config/auth-provider';
// ----------------------------------------------------------------------

export default function App() {
  return (
    <AuthProvider>
    <ThemeProvider>
      <ScrollToTop />
      <StyledChart />
      <Router />
    </ThemeProvider>
    </AuthProvider>
  );
}
