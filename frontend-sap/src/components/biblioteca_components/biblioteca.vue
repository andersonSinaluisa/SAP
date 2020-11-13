<template>
  <v-sheet height="100%" class="overflow-hidden" style="position: relative">
    <menuPrincipal />
    <v-container class="">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="red accent-4 "
            class="white--text"
            dark
            v-bind="attrs"
            v-on="on"
          >
            Agregar documento
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">Nuevo documento</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-form @submit.prevent="guardar" id="guardarDoc">
              <v-row>
                
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="formBiblioteca.autor"
                      color="red accent-4"
                      label="Autor*"
                      required
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="formBiblioteca.descripcion" label="Descripcion*" required></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="9" md="8">
                    <v-file-input
                      v-model="formBiblioteca.documento"
                      color="red accent-4"
                      placeholder="SELECCIONA UN DOCUMENTO*"
                      accept="application/txt"
                      prepend-icon="mdi-file-plus"
                      label="Documento"
                    ></v-file-input>
                  </v-col>
                
              </v-row>
              </v-form>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Cerrar
            </v-btn>
            <v-btn type="submit" form="guardarDoc" color="blue darken-1" text @click="dialog = false">
              Guardar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <br /><br />
      <v-card shaped elevation="2">
        <v-card-title class="white--text red accent-4">
          Mis documentos
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Buscar"
            class="white--text"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="lista_documentos"
            :search="search"
            class="back--text"
            no-data-text="No hay archivos disponibles"
          >
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-container>
  </v-sheet>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
import index from "../principal_components/index";
import menuPrincipal from "../principal_components/menuPrincipal";
export default {
  name: "biblioteca",
  components: { index, menuPrincipal },
  data: () => ({
    search: "",
    api: {
      BIBLIOTECA_API: "http://localhost:8000/BibliotecaApi/",
    },
    dialog: false,
    lista_documentos: [],
    formBiblioteca: {
      id: 0,
      autor: "",
      descripcion: "",
      documento: null,
    },
    headers: [
      { text: "Autor", value: "autor" },
      { text: "Descripcion", value: "descripcion" },
      { text: "Documento", value: "documento" },
      { text: "Fecha subida", value: "fecha_subida" },
    ],
  }),
  methods: {
    guardar() {
      axios
        .post(this.api.BIBLIOTECA_API, this.formBiblioteca)
        .then((response) => {
          if (response.status == 200) {
            swal("Registro guardado", "", "success");
            this.listar();
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    listar() {
      axios
        .get(this.api.BIBLIOTECA_API + "?id=" + this.formBiblioteca.id)
        .then((respuesta) => {
          if (respuesta.status == 200) {
            console.log(respuesta.data);
            this.lista_documentos = respuesta.data;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  beforeCreate: function () {
    if (sessionStorage.length == 0) {
      this.$router.push({ name: "Login" });
    }
  },
  created: function () {
    const usuario = JSON.parse(sessionStorage.getItem("usuario"));
    //console.log(usuario.id_usuario)
    this.formBiblioteca.id = usuario.id_usuario;
    this.listar();
  },
};
</script>

<style>
</style>