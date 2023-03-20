import React, { useEffect } from "react";
import { Helmet } from 'react-helmet-async';
import { Container, Stack, Typography, Button, Box, Tabs, Tab, Grid, Card, CardContent, CardHeader, Divider,LinearProgress,Modal } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';
import Iconify from '../../components/iconify';
import TabPanel from "src/components/tabs/TabPanel";
import { useDispatch, useSelector } from "react-redux";
import { compareLibrary } from "src/redux/library";
import { useAuth } from "src/config/auth-provider";
import TabContent1 from "src/sections/@dashboard/checkLibrary/TabContent1";
function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

export default function CheckLibraryPage() {
  const dispatch = useDispatch();
  const [value, setValue] = React.useState(0);
  const { token } = useAuth();

  const [data, setData] = React.useState({
    file1 : null,
    file2 : null,
  });

  const _result = useSelector((state) => state.library.compareLibrary);
  const [result, setResult] = React.useState(_result);
  const [open, setOpen] = React.useState(false);
  useEffect(() => {
    setResult(_result);
  }, [_result]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleFileChange = (event) => {
    setData({
      ...data,
      [event.target.name]: event.target.files[0],
    });
  };

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const handleSubmit = (event) => {
    dispatch(compareLibrary(data.file1, data.file2, token));

  };

  return (
    <>
      <Helmet>
        <title> Verificar documentos | PlagioGuard </title>
      </Helmet>

      <Container>

        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
          <Typography variant="h4" sx={{ mb: 5 }}>
            Biblioteca
          </Typography>

        </Stack>

        <Stack mb={5} direction="row" alignItems="center" justifyContent="space-between">
          <Box sx={{ width: '100%' }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
              <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
                <Tab label={<Iconify icon="eva:checkmark-circle-outline" />} {...a11yProps(0)} />
                <Tab label={<Iconify icon="eva:checkmark-square-2-outline" />} {...a11yProps(1)} />
                <Tab label={<Iconify icon="eva:checkmark-square-outline" />} {...a11yProps(2)} />
              </Tabs>
            </Box>


            <TabPanel value={value} index={0}>

              <TabContent1 handleFileChange={handleFileChange} handleSubmit={handleSubmit}
                filename1={data.file1 != null ? data.file1.name : null}
                filename2={data.file2 != null ? data.file2.name : null}
               />

            </TabPanel>
            <TabPanel value={value} index={1}>
              <Typography variant="h3" sx={{ mb: 5 }}>

                Comparar un documento nuevo con uno de la biblioteca
              </Typography>

            </TabPanel>
            <TabPanel value={value} index={2}>
              <Typography variant="h3" sx={{ mb: 5 }}>

                Comparar dos documentos de la biblioteca
              </Typography>
               
               <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
                {/*search document 1*/}
                <Typography variant="h5" sx={{ mb: 5 }}>

                  Documento 1 
                  
                </Typography>
                <Button variant="contained" component="label"
                  startIcon={<Iconify icon="bx:bx-search" />} onClick={handleOpen}>
                  buscar documento
                </Button>
              </Stack>
              <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
                {/*search document 1*/}
                <Typography variant="h5" sx={{ mb: 5 }}>

                  Documento 1
                </Typography>
                <Button variant="contained" component="label"
                  startIcon={<Iconify icon="bx:bx-search" />}>
                  buscar documento
                </Button>
              </Stack>
              <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
                <Button variant="contained" component="label"
                  startIcon={<Iconify icon="eva:checkmark-square-outline" />}>
                  Comparar
                </Button>
              </Stack>
            </TabPanel>
          </Box>
        </Stack>
        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
          {result.data != null ? <>

            <Grid container spacing={3}>

              <Card>
                <CardHeader title={<>Porcentaje de similitud:<Typography variant="h4" sx={{ mb: 5 }}>
                  {result.data?.percent}%
                </Typography></>} />
                <Divider />
                {/*progress bar*/}

                <LinearProgress variant="buffer" value={result.data?.percent} />

                <CardContent>
                  <p>
                    {result.data?.text}
                  </p>
                </CardContent>
              </Card>
            </Grid>


          </> : null}
        </Stack>
        <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Container sx={{ width: 500, height: 500, bgcolor: 'background.paper', p: 4, }}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
              Buscar documento
          </Typography>
          <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
              <Grid container spacing={3}>
                <Grid item xs={12}>

                  <Card>
                  </Card>
                  </Grid>
              </Grid>
          </Stack>
        </Container>

      </Modal>
      </Container>
    </>
  )
}