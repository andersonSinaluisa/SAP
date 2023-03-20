// component
import SvgColor from '../../../components/svg-color';

// ----------------------------------------------------------------------

const icon = (name) => <SvgColor src={`/assets/icons/navbar/${name}.svg`} sx={{ width: 1, height: 1 }} />;

const navConfig = [
  {
    title: 'dashboard',
    path: '/app/app',
    icon: icon('ic_analytics'),
  },
  {
    title: 'user',
    path: '/app/user',
    icon: icon('ic_user'),
  },
  {
    title: 'library',
    path: '/app/library',
    icon: icon('ic_library'),
  },
  {
    title: 'check library',
    path: '/app/check-doc',
    icon: icon('ic_check_library'),
  },
  {
    title: 'history',
    path: '/app/history',
    icon: icon('ic_history'),
  },,
];

export default navConfig;
