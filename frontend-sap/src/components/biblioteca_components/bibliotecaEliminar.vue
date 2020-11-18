<template>
  <v-card id="bibliotecaEliminar">
    <v-card-title class="headline"> </v-card-title>
    <v-card-text>
     Eliminar
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="dialog = false">
        Disagree
      </v-btn>
      <v-btn color="green darken-1" text @click="dialog = false"> Agree </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
export default {
  name: "bibliotecaEliminar",
  data: () => ({
    dialog: false,
    formBiblioteca: {
      id: 0,
      autor: "",
      descripcion: "",
      documento: null,
    },
    api: {
      BIBLIOTECA_API: "http://localhost:8000/BibliotecaApi/",
    },
  }),

  props: ["documento","listar"],
  methods: {
    eliminar() {
      const formData = new FormData();
      formData.append(
        "documento",
        this.formBiblioteca.documento,
        this.formBiblioteca.documento.name
      );
      formData.append("autor", this.formBiblioteca.autor);
      formData.append("descripcion", this.formBiblioteca.descripcion);
      formData.append("id", this.formBiblioteca.id);
      axios
        .post(this.api.BIBLIOTECA_API, formData)
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
  },
  beforeCreate: function () {
    if (sessionStorage.length == 0) {
      this.$router.push({ name: "Login" });
    }
  },
  created: function () {
    const usuario = JSON.parse(sessionStorage.getItem("usuario"));
    this.formBiblioteca = this.documento;
  },
};
</script>

<style>
</style>