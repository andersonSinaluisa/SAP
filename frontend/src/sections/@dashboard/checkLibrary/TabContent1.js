import React from "react";
import { Button, Stack, Typography } from "@mui/material";	
import Iconify from '../../../components/iconify';

export default function TabContent1({ handleFileChange, handleSubmit, filename1, filename2 }) {
    return (<>
        <Typography variant="h3" sx={{ mb: 5 }}>
            Comparar dos documentos nuevos
        </Typography>
        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
            <Typography variant="h5" sx={{ mb: 5 }}>
                
                {
                    filename1 != null ? filename1 : "Documento 1"
                }
            </Typography>
            <Button variant="contained" component="label"
                startIcon={<Iconify icon="bx:bx-upload" />}>
                Agregar documento
                <input hidden accept="doc/*" multiple type="file" onChange={handleFileChange} name="file1" />
            </Button>
        </Stack>

        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
            <Typography variant="h5" sx={{ mb: 5 }}>

                {
                    filename2 != null ? filename2 : "Documento 2"
                }
            </Typography>
            <Button variant="contained" component="label"
                startIcon={<Iconify icon="bx:bx-upload" />}>
                Agregar documento
                <input hidden accept="pdf/*;doc/*" multiple type="file" onChange={handleFileChange} name="file2" />
            </Button>
        </Stack>
        <Button variant="contained" component="label"
            startIcon={<Iconify icon="eva:checkmark-circle-outline" />} onClick={handleSubmit}>
            Comparar
        </Button>
    </>)
}