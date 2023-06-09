# inpelsa_v1 
Aplicacion de aprobación y desaprobación de pedidos.
@tavodll

using System;
using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace CRUDExample
{
    public class Customer
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
    }

public class CustomerContext : DbContext
    {
        public DbSet<Customer> Customers { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("YourConnectionString");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            using (var context = new CustomerContext())
            {
                // Create
                var newCustomer = new Customer { Name = "John Doe", Email = "john.doe@example.com" };
                context.Customers.Add(newCustomer);
                context.SaveChanges();
                Console.WriteLine("Nuevo cliente creado.");

                // Read
                var customers = context.Customers.ToList();
                foreach (var customer in customers)
                {
                    Console.WriteLine($"ID: {customer.Id}, Nombre: {customer.Name}, Email: {customer.Email}");
                }

                // Update
                var customerToUpdate = context.Customers.FirstOrDefault(c => c.Id == 1);
                if (customerToUpdate != null)
                {
                    customerToUpdate.Name = "Jane Smith";
                    context.SaveChanges();
                    Console.WriteLine("Cliente actualizado.");
                }

                // Delete
                var customerToDelete = context.Customers.FirstOrDefault(c => c.Id == 1);
                if (customerToDelete != null)
                {
                    context.Customers.Remove(customerToDelete);
                    context.SaveChanges();
                    Console.WriteLine("Cliente eliminado.");
                }
            }

            Console.ReadLine();
        }
    }
}
