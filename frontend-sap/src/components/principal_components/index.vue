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
                  <v-form
                    id="examinarDocumento"
                    class="py-3"
                    @submit.prevent="compararReferencias"
                  >
                    <v-file-input
                      color="red accent-4"
                      placeholder="Selecciona una documento a examinar"
                      id="documento"
                      @change="hasNull(formularioPorReferencia)"
                      accept=".doc,.docx,application/pdf"
                      prepend-icon="mdi-file"
                      label="Documento a examinar"
                      show-size
                      v-model="formularioPorReferencia.archivo"
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
                    @submit.prevent="compararDocumentos"
                  >
                    <v-file-input
                      @change="hasNull(formularioComparar)"
                      v-model="formularioComparar.documentoOrigen"
                      color="red accent-4"
                      placeholder="SELECCIONA UN DOCUMENTO A EXAMINAR*"
                      accept=".doc,.docx,application/pdf"
                      prepend-icon="mdi-file-plus"
                      label="Documento a examinar"
                    >
                    </v-file-input>

                    <v-select
                      @change="hasNull(formularioComparar)"
                      color="red accent-4"
                      :items="lista_Docs"
                      v-model="formularioComparar.id_biblioteca"
                      item-text="documento"
                      item-value="id_biblioteca"
                      single-line
                      auto
                      prepend-icon="mdi-file-plus"
                      label="Seleccionar documento"
                    >
                    </v-select>
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
                  :disabled="hasNull(formularioPorReferencia)"
                  >Examinar documento</v-btn
                >
                <v-btn
                  type="submit"
                  form="formComparardocumentos"
                  color="green accent-4"
                  class="white--text"
                  v-if="step == 2"
                  :disabled="hasNull(formularioComparar)"
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
                <v-col cols="12" sm="12" md="12">
                  <center v-if="printResultadoEstados == 'inicio'">
                    <h3 class="accent-4 red--text">
                      Los resultados se visualizaran aqui.
                    </h3>
                  </center>

                  <center v-if="printResultadoEstados == 'cargando'">
                    <v-progress-circular
                      width="7"
                      size="100"
                      color="red accent-4"
                      indeterminate
                    >
                    </v-progress-circular>
                    <br />
                    <br />
                    <h3 class="red--text accent-4">Examinando documentos...</h3>
                    <center>
                      <h3 class="accent-4 red--text">Resultados.</h3>
                      <br />
                    </center>
                  </center>

                  <center v-if="printResultadoEstados == 'resultados'">
                    <center>
                      <h3 class="accent-4 red--text">Resultados.</h3>
                      <br />
                      <v-row justify="center">
                        <v-col cols="2" sm="2" md="2">
                          <v-img
                            width="150"
                            class="float-right"
                            src="../../statics/img/red-file--v1.png"
                          />
                        </v-col>
                        <v-col cols="6" sm="6" md="6">
                          <div class="py-5">
                            <h3 class="float-left black--text accent-4">
                              Documento: &nbsp;
                              <label class="accent-4 red--text">{{
                                formularioCompararResultados.documentoOrigen
                                  .name
                              }}</label>
                            </h3>
                            <h3 class="float-left black--text accent-4">
                              Documento referencia: &nbsp;
                              <label class="accent-4 red--text">
                                {{
                                  formularioCompararResultados.documentoBiblioteca
                                }}
                              </label>
                            </h3>
                            <br />
                            <h3 class="float-left black--text accent-4">
                              Porcentaje de plagio:
                            </h3>
                            <br />
                            <br />
                            <center>
                              <h1 class="red--text text-accent-4">
                                {{ formularioCompararResultados.resultado }}
                              </h1>
                            </center>
                          </div>
                        </v-col>
                      </v-row>
                      <v-row class="p-5">
                        <v-col cols="12" sm="8" md="6" xl="6">
                          <div class="card border border-3">
                            <label class="accent-4 red--text">
                              {{
                                formularioCompararResultados.documentoBiblioteca
                              }}
                            </label>
                            <br />
                            {{ formularioCompararResultados.text }}
                          </div>
                        </v-col>
                        <v-col cols="12" sm="8" md="6" xl="6">
                          <div class="card border border-3">
                            <label class="accent-4 red--text">{{
                              formularioCompararResultados.documentoOrigen.name
                            }}</label>
                            <br />
                            {{ formularioCompararResultados.text1 }}
                          </div>
                        </v-col>
                      </v-row>
                    </center>
                  </center>

                  <center v-if="printResultadoEstados == 'resultadosRef'">
                    <center>
                      <h3 class="accent-4 red--text">Resultados.</h3>
                      <br />
                      <v-row justify="center">
                        <v-col cols="2" sm="2" md="2">
                          <v-img
                            width="150"
                            class="float-right"
                            src="../../statics/img/red-file--v1.png"
                          />
                        </v-col>
                        <v-col cols="6" sm="6" md="6">
                          <div class="py-5">
                            <h3 class="float-left black--text accent-4">
                              Porcentaje de plagio:
                            </h3>
                            <br />
                            <br />
                            <center>
                              <h1 class="red--text text-accent-4">
                                {{ resultadoComparacionRef.resultado }}
                              </h1>
                            </center>
                          </div>
                        </v-col>
                      </v-row>
                      <v-row
                        class="p-5"
                        v-for="li in resultadoComparacionRef.lista"
                        :key="li"
                      >
                       <v-col cols="12" sm="12" md="12" xl="12">
                         
                          <a :href="li[0]">
                          <span class="blue--text"> Enlace de Referencia: {{ li[0] }}</span>
                          </a>
                        </v-col>
                        

                        <v-col cols="6" sm="6" md="6" xl="6">
                          <h3 class="float-left black--text accent-4">
                            Texto de Referencia:
                          </h3><br>
                          {{ li[1] }}
                        </v-col>
                        <v-col cols="6" sm="6" md="6" xl="6">
                          <h3 class="float-left black--text accent-4">
                            Texto del Documento:
                          </h3><br>

                          {{ li[2] }}
                        </v-col>
                      </v-row>
                    </center>
                  </center>
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
    esValido: false,

    api: {
      BIBLIOTECA_API: "http://localhost:8000/BibliotecaApi/",
      COMPARAR_API: "http://localhost:8000/CompararDocumentoApi/",
      COMPARAR_REF: "http://localhost:8000/ComparaRef/",
    },
    lista_Docs: [],
    tipo_archivo: [".docx", ".pdf"],

    formularioComparar: {
      id_biblioteca: null,
      documentoOrigen: null,
    },

    formularioCompararResultados: {
      documentoOrigen: null,
      documentoBiblioteca: "",
      resultado: "",
      text: "",
      text1: "",
    },

    resultadoComparacionRef: {
      lista: [],
      resultado: [],
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
    printResultado:
      "<h3 class='accent-4 red--text'> Los resultados se visualizaran aqui.</h3>",
    printResultadoEstados: "inicio",
  }),
  methods: {
    hasNull(target) {
      for (var member in target) {
        if (target[member] == null) return true;
      }
      return false;
    },

    validar_boton() {
      if (this.isUrl(this.formularioPorReferencia.ref)) {
        this.esValido = true;
      } else {
        this.esValido = false;
      }
    },

    listar_biblioteca() {
      const usuario = JSON.parse(sessionStorage.getItem("usuario"));
      axios
        .get(this.api.BIBLIOTECA_API + "?id=" + usuario.id_usuario)
        .then((response) => {
          if (response.status == 200) {
            this.lista_Docs = response.data;
            //console.log(this.lista_Docs);
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
      const formData = new FormData();
      this.printResultadoEstados = "cargando";
      formData.append(
        "documenToExaminar",
        this.formularioComparar.documentoOrigen,
        this.formularioComparar.documentoOrigen.name
      );
      formData.append("id_biblioteca", this.formularioComparar.id_biblioteca);
      formData.append("tipo_doc", this.formularioComparar.tipo_doc);
      axios
        .post(this.api.COMPARAR_API, formData)
        .then((response) => {
          this.formularioCompararResultados.resultado = response.data.resultado;
          this.formularioCompararResultados.documentoBiblioteca =
            response.data.documentoBiblioteca;
          this.formularioCompararResultados.documentoOrigen = this.formularioComparar.documentoOrigen;
          this.formularioCompararResultados.text = response.data.corpus_text;
          this.formularioCompararResultados.text1 = response.data.corpus_text1;
          this.printResultadoEstados = "resultados";
        })
        .catch((err) => {
          console.error(err);
        });
    },

    compararReferencias() {
      console.log(this.formularioPorReferencia.referencias);
      const formData = new FormData();
      this.printResultadoEstados = "cargando";
      formData.append("referencia", this.formularioPorReferencia.referencias);
      formData.append(
        "doc",
        this.formularioPorReferencia.archivo,
        this.formularioPorReferencia.archivo.name
      );
      axios
        .post(this.api.COMPARAR_REF, formData)
        .then((res) => {
          console.log(res);
          let element = [];
          let final = [];
          for (let index = 0; index < res.data.corpus_text.length; index++) {
            element.push(res.data.corpus_text[index]);
          }
          this.resultadoComparacionRef.resultado = res.data.resultado;

          this.resultadoComparacionRef.lista = element;
          this.printResultadoEstados = "resultadosRef";
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created: function () {
    this.listar_biblioteca();
  },
};
</script>

<style>
</style>