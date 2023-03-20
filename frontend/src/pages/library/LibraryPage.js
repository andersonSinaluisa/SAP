import { Helmet } from 'react-helmet-async';
import { useEffect, useState } from 'react';
import { Link as RouterLink } from 'react-router-dom';

// @mui
import { Container, Stack, Typography, Button, TextField } from '@mui/material';
// components
import { ProductSort, ProductCartWidget } from '../../sections/@dashboard/products';
import { LibraryFilterSidebar, LibraryList } from '../../sections/@dashboard/library';
import Iconify from '../../components/iconify';

// mock
import PRODUCTS from '../../_mock/products';
import { useAuth } from 'src/config/auth-provider';
import { useDispatch, useSelector } from 'react-redux';
import { getLibraryList } from 'src/redux/library';

// ----------------------------------------------------------------------

export default function LibraryPage() {
  const [openFilter, setOpenFilter] = useState(false);
  const { token } = useAuth();
  const dispatch = useDispatch();

  const [docs, setDocs] = useState([]);
  const _docs = useSelector((state) => state.library.libraryList.data);

  useEffect(() => {
    dispatch(getLibraryList(15, 1, token));
  }, []);

  useEffect(() => {
    setDocs(_docs);
  }, [_docs]);

  const handleOpenFilter = () => {
    setOpenFilter(true);
  };

  const handleCloseFilter = () => {
    setOpenFilter(false);
  };

  return (
    <>
      <Helmet>
        <title> Biblioteca | PlagioGuard </title>
      </Helmet>

      <Container>

        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
          <Typography variant="h4" sx={{ mb: 5 }}>
            Biblioteca
          </Typography>

          <Button to="/app/library/create" size="large" variant="contained" component={RouterLink} startIcon={<Iconify icon="eva:upload-fill" />}>
            Subir documento
          </Button>
        </Stack>

        <Stack mb={5} direction="row" alignItems="center" justifyContent="space-between">
        <TextField label="Buscar" variant="outlined"
        InputProps={{
          endAdornment: (
            <Iconify icon="eva:search-outline" width={20} height={20}
              sx={{ color: 'text.disabled', ml: 1.5 }}
            />
          )
        }}
      />
          <Stack direction="row" spacing={1} flexShrink={0} sx={{ my: 1 }}>
            <LibraryFilterSidebar
              openFilter={openFilter}
              onOpenFilter={handleOpenFilter}
              onCloseFilter={handleCloseFilter}
            />
            <ProductSort />
          </Stack>
        </Stack>

        <LibraryList docs={docs} />
      </Container>
    </>
  );
}
