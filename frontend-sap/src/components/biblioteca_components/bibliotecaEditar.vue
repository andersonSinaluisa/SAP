<template>
    <v-card>
    <v-card-title class="headline"> </v-card-title>
    <v-card-text>
      {{formBiblioteca.documento}}
      Editar
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="dialog = false">
        Disagree
      </v-btn>
      <v-btn color="green darken-1" text @click="dialog = false"> Guardar cambios </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
export default {
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
    guardar_cambios() {
      this.$refs.form.submit()
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
    this.formBiblioteca = this.documento;
    
  },
  mounted: () => {
      
  }
};
</script>

<style>
</style>