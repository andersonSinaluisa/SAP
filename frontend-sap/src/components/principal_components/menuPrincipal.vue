<template >
    <v-app id="menuPrincipal">
        <v-main>
        <v-toolbar color="red accent-4 white--text" dense>
                <v-app-bar-nav-icon color="white" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
                <v-toolbar-title>Sistema Anti-plagio</v-toolbar-title>
                <v-spacer></v-spacer>
        </v-toolbar>
        <v-navigation-drawer color="red accent-4" v-model="drawer" absolute  temporary>
                <v-list-item> 
                    <v-list-item-avatar>
                    <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                    <v-list-item-title class="white--text">{{sessionUsuario.id_persona.nombres }} {{sessionUsuario.id_persona.apellidos}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-divider></v-divider>

                <v-list dense>
                    <v-list-item
                    class="white--text"
                    v-for="item in items"
                    :key="item.title"
                    :to="item.value"
                    link
                    >
                        <v-list-item-icon>
                            <v-icon color="white">{{ item.icon }}</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content
                        class="white--text" >
                            <v-list-item-title>
                                {{ item.title }}
                            </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <v-list-item class="white--text" key="Cerrar sesión" @click.stop="cerrar_sesion" link>
                        <v-list-item-icon>
                            <v-icon color="white">mdi-close-circle</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content class="white--text" >
                            <v-list-item-title>
                                Cerrar sesión
                            </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
        </v-navigation-drawer>
        </v-main>
    </v-app>


</template>

<script>
export default {
    name: 'menuPrincipal',
    data: ()=>({
        sessionUsuario:null,
        drawer: null,
        contenido: "biblioteca",
        items: [
          { title: 'Biblioteca', icon: 'mdi-view-dashboard', value:'biblioteca' },
          //{ title: 'BibliotecaNuevo', icon: 'mdi-view-dashboard', value:'bibliotecaNuevo' },
          //{ title: 'BibliotecaEditar', icon: 'mdi-view-dashboard', value:'bibliotecaEditar' },
          //{ title: 'BibliotecaEliminar', icon: 'mdi-view-dashboard', value:'bibliotecaEliminar' },
          //{ title: 'Inicio', icon: 'mdi-forum', value:'inicio' },
          //{ title: 'Mi perfil', icon: 'mdi-forum', value:'mi_perfil' },
          //{ title: 'Cerrar Sesión', icon: 'mdi-forum', value:'cerrar_sesion' },
        ],
       
    }),
    methods: {

        cerrar_sesion(){
            sessionStorage.clear();
            this.$router.push({name:'Login'})
        }

    },
    beforeCreate: function(){
        if(sessionStorage.length == 0){
            this.$router.push({name:'Login'});
        }
    },
    created: function(){
        this.sessionUsuario = JSON.parse(sessionStorage.getItem('usuario'));
    }
}
</script>

<style>

</style>