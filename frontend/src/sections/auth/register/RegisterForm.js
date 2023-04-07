import { useState } from "react"
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox } from '@mui/material';
import Iconify from '../../../components/iconify';
import { LoadingButton } from '@mui/lab';



export default function RegisterForm (){
    const [data, setData] = useState({
        email: "",
        password: "",
        username: "",
        first_name: "",
        last_name: "",
    })
    const [showPassword, setShowPassword] = useState(false);

    const handleClick = () => {
      };
    
      
      const handleChange = (event) => {
        setData({
          ...data,
          [event.target.name]: event.target.value,
        });
      };
    return (
        <>
      <Stack spacing={3}>
        <TextField name="email" label="Correo" onChange={handleChange}/>
        <TextField name="username" label="Usuario" onChange={handleChange}/>

        <TextField
          name="password"
          label="Contraseña"
          onChange={handleChange}
          type={showPassword ? 'text' : 'password'}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                  <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
      </Stack>

  

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={handleClick}>
        Registrarse
      </LoadingButton>
    </>
    )
}