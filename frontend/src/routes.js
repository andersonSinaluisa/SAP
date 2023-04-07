import { Navigate, useRoutes } from 'react-router-dom';
// layouts
import DashboardLayout from './layouts/dashboard';
import SimpleLayout from './layouts/simple';
//
import BlogPage from './pages/BlogPage';
import UserPage from './pages/users/UserPage';
import LoginPage from './pages/LoginPage';
import Page404 from './pages/Page404';
import LibraryPage from './pages/library/LibraryPage';
import DashboardAppPage from './pages/DashboardAppPage';
import LibraryCreatePage from './pages/library/LibraryCreatePage';
import CheckLibraryPage from './pages/checkLibrary/CheckLibraryPage';
import RegisterPage from './pages/RegisterPage';
// ----------------------------------------------------------------------

export default function Router() {
  const routes = useRoutes([
    {
      path: '/app',
      element: <DashboardLayout />,
      children: [
        { element: <Navigate to="/app/app" />, index: true },
        { path: 'app', element: <DashboardAppPage /> },
        { path: 'user', element: <UserPage /> },
        { path: 'library', element: <LibraryPage /> },
        {path: 'library/create', element: <LibraryCreatePage /> },
        { path: 'check-doc', element: <CheckLibraryPage /> },
        { path: 'history', element: <BlogPage /> },
      ],
    },
    {
      path: '/',
      element: <SimpleLayout />,
      children: [
        { element: <Navigate to="/app/app" />, index: true },
        { path: '404', element: <Page404 /> },
        { path: '*', element: <Navigate to="/404" /> },
        { path: 'login', element: <LoginPage /> },
        {path:'registro',element:<RegisterPage/>}
      ],
    },
    {
      path: '*',
      element: <Navigate to="/404" replace />,
    },
  ]);

  return routes;
}
