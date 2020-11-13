<template>
  <v-sheet height="100%" class="overflow-hidden" style="position: relative">
    <menuPrincipal />

    <v-container class="">
      <v-row>
        <v-col cols="12">
          <v-card elevation="2" shaped>
            <v-card-title class="red accent-4 white--text">
              Examinar documento
            </v-card-title>
            <v-card-text>
              <v-tabs centered>
                <v-tab class="red--text" @click="step = 1"
                  >Examinar documento</v-tab
                >
                <v-tab @click="step = 2" class="red--text"
                  >Comparar documento</v-tab
                >
              </v-tabs>
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-form id="examinarDocumento" class="py-3" @submit.prevent="mostrarBibliografia = true; mostrar=false;">
                    <v-file-input
                      color="red accent-4"
                      placeholder="Selecciona una documento a examinar"
                      id="documento"
                      accept="application/msword,application/pdf"
                      prepend-icon="mdi-file"
                      label="Documento a examinar"
                      show-size
                    >
                    </v-file-input>

                    <v-dialog v-model="dialog" persistent max-width="600px">
                      <template v-slot:activator="{ on, attrs }">
                        <a href="#" class="blue--text" v-bind="attrs" v-on="on">
                          <v-icon>mdi-plus</v-icon>
                          <strong>Agregar referencias.</strong>
                        </a>
                      </template>
                      <v-card>
                        <v-card-title>
                          <span class="headline"
                            >Ingresa las referencia bibliografica a
                            utilizar.</span
                          >
                        </v-card-title>
                        <v-card-text>
                          <v-container>
                            <v-row>
                              <v-col cols="12" sm="12" md="12">
                                <v-form
                                  v-model="esValido"
                                  ref="referenciaForm"
                                  id="referenciaForm"
                                  @submit.prevent="guardar_referencia"
                                >
                                  <v-text-field
                                    color="red accent-4"
                                    :rules="rules.textRules"
                                    v-model="formularioPorReferencia.ref"
                                    @keyup="validar_boton"
                                    @change="validar_boton"
                                    required
                                    label="Referencia *"
                                  >
                                  </v-text-field>
                                </v-form>
                              </v-col>
                            </v-row>
                          </v-container>
                        </v-card-text>
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="dialog = false"
                          >
                            Cerrar
                          </v-btn>

                          <v-btn
                            color="blue darken-1"
                            text
                            type="submit"
                            form="referenciaForm"
                            :disabled="!this.esValido"
                          >
                            Guardar
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>

                    <ul>
                      <li
                        class=""
                        v-for="li in formularioPorReferencia.referencias"
                        :key="li"
                      >
                        <a :href="li">
                          <span class="blue--text">{{ li }}</span>
                        </a>
                        &nbsp;
                        <v-icon color="red accent-4" @click="borrar_ref(li)"
                          >mdi-delete</v-icon
                        >
                      </li>
                    </ul>
                  </v-form>
                </v-window-item>

                <v-window-item :value="2">
                  <v-form
                    id="formComparardocumentos"
                    @submit.prevent="mostrar = true; mostrarBibliografia = false"
                  >
                    <v-file-input
                      v-model="formularioComparar.documentoOrigen"
                      color="red accent-4"
                      placeholder="SELECCIONA UN DOCUMENTO A EXAMINAR*"
                      accept="application/txt"
                      prepend-icon="mdi-file-plus"
                      label="Documento a examinar"
                    >
                    </v-file-input>

                    <v-file-input
                      v-model="formularioComparar.documento"
                      color="red accent-4"
                      id="documento"
                      name="documento"
                      placeholder="SELECCIONA UN DOCUMENTO REFERENCIA*"
                      accept="application/txt"
                      prepend-icon="mdi-file-search"
                      label="Documento a examinar"
                    >
                    </v-file-input>
                  </v-form>
                </v-window-item>
              </v-window>
            </v-card-text>
            <v-card-actions>
              <div class="center">
                <v-btn
                  form="examinarDocumento"
                  type="submit"
                  color="green accent-4"
                  class="white--text"
                  v-if="step == 1"
                  >Examinar documento</v-btn
                >
                <v-btn
                  type="submit"
                  form="formComparardocumentos"
                  color="green accent-4"
                  class="white--text"
                  v-if="step == 2"
                >
                  Comparar documentos
                </v-btn>
              </div>
            </v-card-actions>

            <v-card-subtitle>
              <v-alert v-if="step == 1" dense type="info">
                <strong>
                  Selecciona un documento a examinar y referencias
                  bibliograficas para examinar el documento basado en las
                  referencias ingresadas.
                </strong>
              </v-alert>

              <v-alert v-if="step == 2" dense type="info">
                <strong>
                  Compara los resultados con los documentos guardados en tu
                  biblioteca.
                </strong>
              </v-alert>
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card shaped>
            <v-card-title class="red accent-4 white--text"
              >Resultados</v-card-title
            >
            <v-card-text>
              <v-row justify="center">
                <v-col cols="4">
                  <v-img
                    class="float-right"
                    src="../../statics/img/red-file--v1.png"
                    width="150"
                  />
                </v-col>
                <v-col cols="8">
                  <div class="float-left py-5">
                    <h3 v-if="mostrar">
                      RESUTADOS DE:
                      <strong class="red--text accent-4">{{resultados.nombre}}</strong>
                    </h3>
                    <h3 v-if="mostrar">
                      DOCUMENTO REFERENCIA:
                      <strong class="red--text accent-4">{{
                        resultados.comparadoCon
                      }}</strong>
                    </h3>
                    <h3 v-if="mostrar">PORCENTAJE DE PLAGIO:</h3>
                    <br v-if="mostrar" />
                    <center>
                      <h1 v-if="mostrar" class="center">
                        <strong class="red--text accent4">
                          {{ resultados.total }} %
                        </strong>
                      </h1>
                    </center>




                    <h3 v-if="mostrarBibliografia">
                      RESUTADOS DE:
                      <strong class="red--text accent-4">{{resultadosBibiografia.nombre}}</strong>
                    </h3>

                    <h3 v-if="mostrarBibliografia">
                      REFERENCIAS BIBLIOGRAFICAS:
                      <ul v-if="mostrarBibliografia">
                          <li v-for="l in formularioPorReferencia.referencias" :key="l">
                              <a :href="l">{{l}}</a>
                          </li>
                      </ul>
                    </h3>
                    <h3 v-if="mostrarBibliografia">PORCENTAJE DE PLAGIO:</h3>
                    <br v-if="mostrarBibliografia" />
                    <center>
                      <h1 v-if="mostrarBibliografia" class="center">
                        <strong class="red--text accent4">
                          {{ resultadosBibiografia.total }} %
                        </strong>
                      </h1>
                    </center>

                  </div>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-sheet>
</template>

<script>
import axios from "axios";
import menuPrincipal from "./menuPrincipal";
export default {
  name: "index",
  components: { menuPrincipal },
  data: () => ({
    step: 1,
    dialog: false,
    mostrar: false,
    mostrarBibliografia: false,
    esValido: false,
    listaDocs: [],
    api: {
      BIBLIOTECA_API: "http://localhost:8000/BibliotecaApi/",
      COMPARAR_API: "http://localhost:8000/CompararDocumentoApi/",
    },
    formularioComparar: {
      documentoOrigen: null,
      documento: null,
    },
    resultados: {
      nombre: "documento.word",
      total: 35,
      comparadoCon: "documento.word",
    },
    resultadosBibiografia: {
      nombre: "documento.word",
      total: 35,
      comparadoCon: "documento.word",
    },
    formularioPorReferencia: {
      archivo: null,
      ref: "",
      referencias: [],
    },

    rules: {
      docRules: [
        (v) =>
          !v ||
          v.size < 10000000 ||
          "El tamaño de la foto debe ser menos a los 2mb.",
      ],
      textRules: [(v) => !!v || "Este campo es requerido"],
    },
  }),
  methods: {
    validar_boton() {
      if (this.isUrl(this.formularioPorReferencia.ref)) {
        this.esValido = true;
      } else {
        this.esValido = false;
      }
    },

    listar_bibioteca() {
      const usuario = JSON.parse(sessionStorage.getItem("usuario"));
      axios
        .get(this.api.BIBLIOTECA_API + "?id=" + usuario.id_usuario)
        .then((response) => {
          if (response.status == 200) {
            this.listaDocs = response.data;
            console.log(this.listaDocs);
          }
        });
    },
    guardar_referencia() {
      this.formularioPorReferencia.referencias.push(
        this.formularioPorReferencia.ref
      );
      this.formularioPorReferencia.ref = "";
    },
    borrar_ref(ref) {
      const elemento = this.formularioPorReferencia.referencias.indexOf(ref);
      if (elemento > -1) {
        this.formularioPorReferencia.referencias.splice(ref);
      }
    },
    isUrl(s) {
      var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
      return regexp.test(s);
    },
    compararDocumentos() {
      console.log(this.formularioComparar);
      /* 
        var data = new FormData('#formComparardocumentos');
        console.log(data);
        axios.post(this.api.COMPARAR_API,this.formularioComparar,{'Content-Type': 'multipart/form-data'}).then((response) =>{
          if (response.status == 200) {
              console.log(response);
          }
        });
        */
    },
  },
  created: function () {
    this.listar_bibioteca();
  },
};
</script>

<style>
</style>