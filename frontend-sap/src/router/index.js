import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../components/seguridad-components/Login.vue'
import menuPrincipal from '../components/principal_components/menuPrincipal.vue'
import index from '../components/principal_components/index.vue'
import biblioteca from '../components/biblioteca_components/biblioteca.vue';
import bibliotecaNuevo from '../components/biblioteca_components/bibliotecaNuevo.vue';
import bibliotecaEditar from '../components/biblioteca_components/bibliotecaEditar.vue';
import bibliotecaEliminar from '../components/biblioteca_components/bibliotecaEliminar.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/menu',
    name: 'menu',
    component: menuPrincipal
  },
  {
    path: '/index',
    name: 'index',
    component: index
  },

  {
    path: '/biblioteca',
    name: 'biblioteca',
    component: biblioteca
  },


  {
    path: '/bibliotecaNuevo',
    name: 'bibliotecaNuevo',
    component: bibliotecaNuevo
  },


  {
    path: '/bibliotecaEditar',
    name: 'bibliotecaEditar',
    component: bibliotecaEditar
  },

  {
    path: '/bibliotecaEliminar',
    name: 'bibliotecaEliminar',
    component: bibliotecaEliminar
  },



  {
    path: '/About',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
