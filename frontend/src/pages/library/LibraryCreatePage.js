import React, { useEffect, useState } from 'react';
import { Helmet } from 'react-helmet-async';
import { Container, Stack, Typography, TextField,Button } from '@mui/material';
import Iconify from '../../components/iconify';
import { Link as RouterLink, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { createLibrary,CREATE_LIBRARY } from 'src/redux/library';
import { useAuth } from 'src/config/auth-provider';


export default function LibraryCreatePage() {

    const dispatch = useDispatch();
    const navigate = useNavigate(); 
    const {token} = useAuth();
    const _createLibrary = useSelector((state) => state.library.createLibrary);
    const [values, setValues] = useState({
        author: '',
        file:null,
        description: '',
        title: '',
    });


    useEffect(() => {
        if (_createLibrary.status === 201) {
            dispatch({
                type: CREATE_LIBRARY,
                payload: {
                    data: null,
                    status: 0,
                    error: ""
                }})
            navigate('/app/library', { replace: true });
        }
    }, [_createLibrary]);
    
    

    const handleChange = (event) => {
        setValues({
            ...values,
            [event.target.name]: event.target.value,
        });
    };


    const handleFileChange = (event) => {
        setValues({
            ...values,
            file: event.target.files[0],
        });
    };


    const handleSubmit = (event) => {
        
        dispatch(createLibrary(
            values.title,
            values.author,
            values.description,
            values.file,
            token
        ))
    
    }
    return (
        <>
            <Helmet>
                <title> Nuevo documento | PlagioGuard </title>
            </Helmet>

            <Container>
                <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
                    <Typography variant="h4" sx={{ mb: 5 }}>
                        Nuevo documento
                    </Typography>

                </Stack>
                <Stack direction="row" alignItems="center" sx={{ mb: 5 }} spacing={3}>


                    <TextField name="author" label="Autor" onChange={handleChange} />
                    <TextField name="title" label="Título" onChange={handleChange} />

                    <TextField name="description" label="Descripción" onChange={handleChange} multiline
                        maxRows={4}
                    />
                    <Button variant="contained" component="label"
                        startIcon={<Iconify icon="bx:bx-upload" />}>
                        Upload
                        <input hidden accept="pdf/*;doc/*" multiple type="file" onChange={handleFileChange}/>
                    </Button>

                </Stack>

                <Stack direction="row" alignItems="center" sx={{ mb: 5 }} spacing={3}>

                    {/* cancel button */}
                    <Button variant="contained" color="error" type="submit" to="/app/library"  component={RouterLink} >
                        Cancelar
                    </Button>
                    {/* submit button */}
                    <Button variant="contained" color="primary" type="submit" sx={{ mt: 3, ml: 1 }} onClick={handleSubmit}>
                        Guardar
                    </Button>
                </Stack>
            </Container>
        </>
    )
}