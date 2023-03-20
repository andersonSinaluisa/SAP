import PropTypes from 'prop-types';
// @mui
import { Grid } from '@mui/material';
import DocCard from './DocCard';

// ----------------------------------------------------------------------

LibraryList.propTypes = {
  docs: PropTypes.array.isRequired,
};

export default function LibraryList({ docs, ...other }) {
  return (
    <Grid container spacing={3} {...other}>
      {docs.map((doc) => (
        <Grid key={doc.id_biblioteca} item xs={12} sm={6} md={3}>
          <DocCard doc={doc} />
        </Grid>
      ))}
    </Grid>
  );
}
