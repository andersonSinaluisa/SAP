<template >
<v-app style="background-color: #1F2D41;">
    <v-main>
        <v-container class="fill-height" >
           <v-row align="center" justify="center">
               <v-col cols="12" sm="8" md="8">
                   <v-card  class="elevation-12">
                       <v-window v-model="step">
                           <v-window-item :value="1">
                               <v-row>
                                    <v-col cols="12" md="6">
                                        <v-card-text class="mt-12">
                                            <center>
                                            <h5 class="green--text center text--accent-3 display-2">
                                                Iniciar Sesión
                                            </h5>
                                            </center>
                                        
                                         <v-form @submit.prevent="login" id="form-login">
                                            <v-text-field
                                                required
                                                v-model="loginFormulario.correo"
                                                label="Correo electronico"
                                                name="correo"
                                                type="text"
                                                color="red accent-3"
                                            >                                                
                                            </v-text-field>
                                            
                                            <v-text-field
                                                required
                                                v-model="loginFormulario.clave"
                                                label="Contraseña"
                                                name="clave"   
                                                type="password"
                                                color="red accent-3"
                                            ></v-text-field>

                                            <div class="text-center mt-3">
                                                <v-btn type="submit" submit="form-login"  color="green accent-3" dark>Iniciar Sesión</v-btn>
                                            </div>
                                            
                                        </v-form>

                                        </v-card-text>
                                     

                                    </v-col>
                                    <v-col cols="12"  class="red accent-3" md="6">
                                        <v-card-text class="white--text mt-12">
                                            <center>
                                                <v-img class="py-0 center" width="150" height="150"  src="../../statics/img/logoFormulario.png"></v-img>
                                            </center>

                                            <h1 class="text-center display-1">Bienvenido!!</h1>
                                            <h3 class="text-center">Ingresa tus credenciales para comenzar. <br/> Si no tienes una cuenta, registrate.</h3>
                                            <div class="text-center py-5">
                                                <v-btn color="blue accent-3 white--text"  @click="step++">Crearme una cuenta</v-btn>
                                            </div>
                                        </v-card-text>

                                    </v-col>    
                               </v-row>
                           </v-window-item>
                           <v-window-item :value="2">
                               <v-row class="fill-height">
                                   <v-col cols="12" sm md="5" class="red accent-3">
                                            <center>
                                               <v-img class="py-0" width="250" height="250" aspect-ratio="1" src="../../statics/img/logoFormulario.png"></v-img>
                                           </center>
                                       <v-card-text class="white--text mt-12">
                                        

                                           
                                           <h1 class="text-center display-1">Bienvenido!!</h1>
                                           <h3 class="text-center">Para usar nuestros servicios, inicia sesión con tu información personal. </h3>
                                       </v-card-text>
                                       <div class="text-center">
                                           <v-btn class="blue accent-3 white--text" @click="step--">Iniciar Sesión</v-btn>
                                       </div>
                                   </v-col>

                                   <v-col cols="12" md="7">
                                        <center>
                                                <h1 class="green--text text--accent-3" > Registrate </h1>
                                                <v-avatar size="200">
                                                    
                                                    <v-img 
                                                        src="../../statics/img/altFoto.png"
                                                        width="50"
                                                    >
                                                    </v-img>
                                                </v-avatar>
                                        </center>
                                       <v-form @submit.prevent="guardar_usuario"  id="form-crear-usuario">
                                           <div class=" py-5 px-5 row justify-content-center">
                                               <div class="col-6">
                                                   <v-text-field
                                                        v-model="formulario.nombres"
                                                        required
                                                        label="Nombres"
                                                        :rules="rules.textRules"
                                                        name="nombres"
                                                        id="nombres"
                                                        color="red accent-3"
                                                        type="text"
                                                        >
                                                    </v-text-field>
                                               </div>
                                               <div class="col-6">
                                                   <v-text-field
                                                        required
                                                        v-model ="formulario.apellidos"
                                                         :rules="rules.textRules"
                                                        label="Apellidos"
                                                        name="apellidos"
                                                        id="apellidos"
                                                        color="red accent-3"
                                                        type="text"
                                                        >
                                                    </v-text-field>
                                               </div>
                                               <div class="col-6">
                                                   <v-text-field
                                                        required
                                                        v-model ="formulario.identificacion"
                                                        label="Identificación"
                                                        :rules="[]"
                                                        name="identificación"
                                                        id="identificación"
                                                        color="red accent-3"
                                                        type="text"
                                                        >
                                                    </v-text-field>

                                               </div>

                                                <div class="col-6">
                                                    <v-file-input
                                                            :rules="rules.fotoRules"
                                                            v-model="formulario.foto"
                                                            color="red accent-3"
                                                            accept="image/png, image/jpeg, image/bmp"
                                                            placeholder="Selecciona una foto de perfil"
                                                            id="foto"
                                                            prepend-icon="mdi-camera"
                                                            label="Foto de perfil">
                                                    </v-file-input>
                                                </div>

                                               <div class="col-6">
                                                   <v-text-field
                                                        required
                                                        v-model="formulario.correo"
                                                        :rules="[]"
                                                        label="Correo Electronico"
                                                        name="correo"
                                                        id="correo"
                                                        color="red accent-3"
                                                        type="email"
                                                        >
                                                    </v-text-field>
                                               </div>

                                               <div class="col-6">
                                                   <v-text-field
                                                        required
                                                        :rules="[vl_validaClave]"
                                                        label="Contraseña"
                                                        v-model="formulario.clave"
                                                        name="clave"
                                                        id="clave"
                                                        color="red accent-3"
                                                        type="password"
                                                        >
                                                    </v-text-field>
                                               </div>

                                               <div class="col-6">
                                                   <v-text-field
                                                        required
                                                        :rules="[vl_confClave(this.formulario.clave,this.formulario.cnf_clave)]"
                                                        label="Confirmar contraseña"
                                                        v-model="formulario.cnf_clave"
                                                        name="cnf_clave"
                                                        id="cnf_clave"
                                                        color="red accent-3"
                                                        type="password"
                                                        >
                                                    </v-text-field>
                                               </div>
                                               
                                           </div>
                                           <center class="px-5">
                                                <v-btn type="submit" form="form-crear-usuario"  class="red accent-3 white--text" >Crear mi cuenta</v-btn>
                                           </center>
                                       </v-form>
                                   </v-col>
                               </v-row>
                              
                           </v-window-item>
                       </v-window>

                   </v-card>
               </v-col>
           </v-row>
             <div class="text-center">
                                    <v-snackbar
                                        v-model="snackbar">
                                        {{ text }}
                                        <template v-slot:action="{ attrs }">
                                             <v-btn
                                                color="blue"

                                                text
                                                v-bind="attrs"
                                                @click="snackbar = false">Ok.
                                            </v-btn>
                                        </template>
                                    </v-snackbar>
            </div>    
        </v-container>
    </v-main>
</v-app>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'
export default {
    data: () => ({
        step: 1,
        valid: true,
        snackbar: false,
        text: 'Error interno del servidor, intentelo mas tarde.',
        timeout: 2000,
        myImage: "../../statics/img/logoFormulario.png",
        fotoSrc: "../../statics/img/altFoto.png",

        api:{
            USUARIO_API : "http://localhost:8000/UsuarioApi/",
            LOGIN_API : "http://localhost:8000/SeguridadApi/",
        },


        loginFormulario:{
            correo: '',
            clave: ''
        },


        formulario: {
            nombres:'',
            apellidos:'',
            identificacion:'',
            correo:'',
            clave:'',
            cnf_clave:'',
            foto: null
        },

        

        rules: {
            fotoRules: [v => !v || v.size < 2000000 || 'El tamaño de la foto debe ser menos a los 2mb.'],
            textRules: [v => !!v || 'Este campo es requerido',],
            IdentificacionRules: [v => !!v  || 'Debe contener al menos 10 caracteres',],
        }
}),
    methods:{

        vl_identificacion(v){
            if(v.lenght <= 10){
                return true;
            }else{
                return "Identificación no valida";
            }
        },

        vl_validaClave(v){
            var bandera = false
            var exp = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/;
            if( !(exp.test(v) && v.length >= 8) ){
                return "La contraseña debe contener 8 caracteres entre letras y numeros."
            }else{
                return true
            }
        },

        vl_confClave(v,confContra){
            if(!(v == confContra)){
                 return "La contraseña debe coincidir con la confirmación.";
            }else{
                return true
            }
        },

        vl_previewFoto(){

        },

        guardar_usuario(){
            axios.post(this.api.USUARIO_API,this.formulario).then((respuesta) => {
                if(respuesta.status == 200){
                    this.step--;
                    this.snackbar = true;
                    this.text = 'Usuario creado exitosamente. Ingrese al sistemausando las credenciales ingresadas.'
                    this.formulario =  {
                        nombres:'',
                        apellidos:'',
                        identificacion:'',
                        correo:'',
                        clave:'',
                        cnf_clave:'',
                        foto: null
                    }
                }else{
                    this.snackbar = true;
                }
            });
        },

         login(){
            axios.post(this.api.LOGIN_API,this.loginFormulario).then((respuesta) => {
                if(respuesta.status == 200){
                    var usuario = respuesta.data;
                    this.text = 'Usuario creado exitosamente. Ingrese al sistemausando las credenciales ingresadas.'
                    swal("Bienvenido "+usuario.id_persona.nombres+" "+usuario.id_persona.apellidos,"","success");
                    sessionStorage.setItem('usuario', JSON.stringify(usuario));
                    setTimeout(() => this.$router.push({ name: 'index' }), 2000);
                    this.loginFormulario = {
                        correo: '',
                        clave: ''
                    }
                    //var obj = JSON.parse(sessionStorage.usuario);
                    //console.log(obj)
               }else{
                    this.text = 'Usuario o contraseña incorrectos.'
                    this.snackbar = true;
                }
            });
        }





    },
    props: {
        source: String
    },
    beforeCreate: function(){
        console.log('Hola')
    }
}
</script>

<style>

</style>