  <template>
  <v-container class="">
    <v-dialog v-model="dialog"  max-width="600px">
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
                  <v-text-field
                    v-model="formBiblioteca.descripcion"
                    label="Descripcion*"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="12" sm="9" md="8">
                  <v-file-input
                    v-model="formBiblioteca.documento"
                    color="red accent-4"
                    placeholder="SELECCIONA UN DOCUMENTO*"
                    accept="application/msword,application/pdf"
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
          <v-btn
            type="submit"
            form="guardarDoc"
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Guardar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
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
  
  props:['listar'],
  methods: {
    guardar() {
      const formData = new FormData();
      formData.append("documento", this.formBiblioteca.documento,this.formBiblioteca.documento.name);
      formData.append("autor",this.formBiblioteca.autor);
      formData.append("descripcion",this.formBiblioteca.descripcion);
      formData.append("id",this.formBiblioteca.id)
      axios.post(this.api.BIBLIOTECA_API,formData).then((response) => {
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
    this.formBiblioteca.id = usuario.id_usuario;
    
  },
};
</script>

<style>
</style>