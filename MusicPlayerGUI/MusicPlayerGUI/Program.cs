using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace MusicPlayerGUI
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
<<<<<<< Updated upstream
            Application.Run(new MusicPlayerMainView());
=======
            Application.Run(new Form1());
>>>>>>> Stashed changes
        }
    }
}
