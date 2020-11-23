<template>
  <v-sheet height="100%" class="overflow-hidden" style="position: relative">
    <menuPrincipal />
    <bibliotecaNuevo :listar="listar"> </bibliotecaNuevo>
    <v-container class="">
      <v-card shaped elevation="2">
        <v-card-title class="white--text red accent-4">
          Mis documentos
          <v-spacer></v-spacer>
        </v-card-title>

        <v-simple-table class="">
          <template v-slot:default>
            <thead class="red accent-4 white--text">
              <tr>
                <th class="white--text">Autor</th>
                <th class="white--text">Descripcion</th>
                <th class="white--text">Documento</th>
                <th class="white--text">Fecha subida</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="d in lista_documentos" :key="d.id_biblioteca">
                <td>{{ d.autor }}</td>
                <td>{{ d.descripcion }}</td>
                <td>
                  <a :href="api.local_media + d.documento" target="_blank">
                    {{ d.documento }}</a
                  >
                </td>
                <td>{{ d.fecha_subida }}</td>
                <td class="">
                  <v-btn
                    color="blue accent-4"
                    @click="
                      dialog_edit = true;
                      llenar_formulario(d);
                    "
                    rounded
                  >
                    <v-icon class="white--text"
                      >mdi mdi-file-document</v-icon
                    > </v-btn
                  >&nbsp;
                  <v-btn
                    color="orange accent-4"
                    @click="
                      dialog_delete = true;
                      llenar_formulario(d);
                    "
                    rounded
                  >
                    <v-icon class="white--text">mdi-delete-empty</v-icon>
                  </v-btn>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>

      <v-dialog v-model="dialog_delete" max-width="600">
        <v-card>
          <v-card-title class="red accent-4 white--text"
            >Estas seguro que quieres eliminar este documento?
          </v-card-title>
          <v-card-text>
            <v-row align="center">
              <v-col cols="12">
                <div class="black--text float-left">
                  Documento: {{ api.local_media + form_edit.display_doc }} <br />
                  Autor:  {{ form_edit.autor }} <br />
                  Descripción: {{ form_edit.descripcion }} <br />
                  Fecha subida: {{ form_edit.fecha_subida }}
                </div>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-col cols="12" class="" sm="12" md="12">
              <center>
                <v-btn
                  color="red accent-4"
                  @click="borrar_doc(form_edit.id)"
                  class="white--text"
                  >Eliminar</v-btn
                >
                <v-btn
                  color="blue accnet-4"
                  @click="dialog_delete = false"
                  class="white--text ml-4"
                  >Cancelar</v-btn
                >
              </center></v-col>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="dialog_edit" max-width="600">
        <v-card>
          <v-card-title class="red accent-4 white--text">
            Editar documento
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="editar_doc" id="editarDoc">
              <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="form_edit.autor"
                    color="red accent-4"
                    label="Autor*"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="form_edit.descripcion"
                    label="Descripcion*"
                    color="red accent-4"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="12" sm="9" md="8">
                  <v-file-input
                    v-model="form_edit.documento"
                    color="red accent-4"
                    placeholder="SELECCIONA UN DOCUMENTO*"
                    accept="application/msword,application/pdf"
                    prepend-icon="mdi-file-plus"
                    label="Nuevo Documento"
                  ></v-file-input>
                </v-col>
                <v-col cols="12" sm="9" md="8">
                  <strong>Documento actual*</strong> <br />
                  <a :href="form_edit.display_doc">{{ form_edit.display_doc }}</a>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-row>
              <v-col cols="12" class="" sm="12" md="12">
                <center>
                  <v-btn
                    color="red accent-4"
                    form="editarDoc"
                    type="submit"
                    class="white--text"
                    >Guardar cambios</v-btn
                  >
                  <v-btn
                    color="blue accnet-4"
                    @click="dialog_edit = false"
                    class="white--text ml-4"
                    >Cancelar</v-btn
                  >
                </center>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </v-sheet>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
import index from "../principal_components/index";
import menuPrincipal from "../principal_components/menuPrincipal";
import bibliotecaNuevo from "./bibliotecaNuevo";
export default {
  name: "biblioteca",
  components: {
    index,
    menuPrincipal,
    bibliotecaNuevo,
  },
  data: () => ({
    search: "",
    dialog_edit: false,
    dialog_delete: false,
    doc_obj: {},
    api: {
      BIBLIOTECA_API: "http://localhost:8000/BibliotecaApi/",
      local_media: "http://localhost:8000",
    },

    form_edit: {
      id: 0,
      autor: "",
      descripcion: "",
      fecha_subida: "",
      documento: null,
      display_doc: null
    },

    lista_documentos: [],
    id: 0,
    headers: [
      { text: "Autor", value: "autor" },
      { text: "Descripcion", value: "descripcion" },
      { text: "Documento", value: "documento" },
      { text: "Fecha subida", value: "fecha_subida" },
    ],
  }),
  methods: {
    borrar_doc(id) {
    

      axios
        .delete(this.api.BIBLIOTECA_API + "?id=" + id)
        .then((response) => {
          if (response.status == 200) {
            swal("Registro eliminado", "", "warning");
            this.dialog_delete = false;
            this.listar();
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    editar_doc() {
      var formdata = new FormData();
      //console.log(this.form_edit.documento)
      formdata.append("documento", this.form_edit.documento,this.form_edit.documento.name);
      formdata.append("id",this.form_edit.id);
      formdata.append("autor",this.form_edit.autor);
      formdata.append("descripcion",this.form_edit.descripcion);
      
      axios
        .put(this.api.BIBLIOTECA_API,formdata)
        .then((response) => {
          if (response.status == 200) {
            swal("Registro actualizado", "", "success");
            this.dialog_edit = false;
            this.listar();
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    llenar_formulario(documento) {
      this.form_edit.id = documento.id_biblioteca;
      this.form_edit.autor = documento.autor;
      this.form_edit.fecha_subida = documento.fecha_subida;
      this.form_edit.descripcion = documento.descripcion;
      this.form_edit.display_doc = this.api.local_media + documento.documento;
    },
    listar() {
      axios
        .get(this.api.BIBLIOTECA_API + "?id=" + this.id)
        .then((respuesta) => {
          if (respuesta.status == 200) {
            //console.log(respuesta.data);
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
    this.id = usuario.id_usuario;
    this.listar();
  },
};
</script>

<style>
</style>