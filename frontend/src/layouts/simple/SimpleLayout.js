import { Outlet, Navigate } from 'react-router-dom';
// @mui
import { styled } from '@mui/material/styles';
import { useAuth } from '../../config/auth-provider';

// components
import Logo from '../../components/logo';

// ----------------------------------------------------------------------

const StyledHeader = styled('header')(({ theme }) => ({
  top: 0,
  left: 0,
  lineHeight: 0,
  width: '100%',
  position: 'absolute',
  padding: theme.spacing(3, 3, 0),
  [theme.breakpoints.up('sm')]: {
    padding: theme.spacing(5, 5, 0),
  },
}));

// ----------------------------------------------------------------------

export default function SimpleLayout() {

  const { token } = useAuth();
  
  

  if (token) {
    return <Navigate to="/app" />;
  }
  
  
  
  return (
    <>
      <StyledHeader>
        <Logo />
      </StyledHeader>

      <Outlet />
    </>
  );
}
